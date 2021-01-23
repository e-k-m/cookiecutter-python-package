from pathlib import Path
import shutil
import unittest

import common


class TestBake(unittest.TestCase):
    def setUp(self):
        self.output_dir = Path("./cookies")

        def output_factory(s):
            p = self.output_dir / Path(s)
            return p

        self.cookies = common.Cookies(".", output_factory, "")

    def tearDown(self):
        shutil.rmtree(self.output_dir)

    def test_bake_with_defaults(self):
        with common.bake_in_temp_dir(self.cookies) as result:
            self.assertTrue(result.project.is_dir())
            self.assertEqual(result.exit_code, 0)
            self.assertIs(result.exception, None)
            self.assertSetEqual(
                set([f.name for f in result.project.iterdir()]),
                set(
                    [
                        ".github",
                        ".gitignore",
                        "MANIFEST.in",
                        "README.md",
                        "batsay",
                        "noxfile.py",
                        "setup.cfg",
                        "setup.py",
                        "tests",
                        "pyproject.toml",
                    ]
                ),
            )

    def test_bake_and_run_nox(self):
        with common.bake_in_temp_dir(self.cookies) as result:
            self.assertTrue(result.project.is_dir())
            # NOTE: Nox in nox, -- maybe a better way, but for KISS now.
            self.assertEqual(
                common.run_inside_dir("nox -s test-3.7", str(result.project)),
                0,
            )
            self.assertEqual(
                common.run_inside_dir("nox -s fmt", str(result.project)), 0,
            )
            self.assertEqual(
                common.run_inside_dir("nox -s lint", str(result.project)), 0,
            )

    def test_bake_with_no_console_script(self):
        with common.bake_in_temp_dir(
            self.cookies, extra_context={"command_line_interface": "n"}
        ) as result:
            setup_path = result.project / "setup.py"
            with open(setup_path, "r") as f:
                self.assertNotIn("entry_points", f.read())

    def test_bake_with_console_script(self):
        with common.bake_in_temp_dir(
            self.cookies, extra_context={"command_line_interface": "y"}
        ) as result:
            setup_path = result.project / "setup.py"
            with open(setup_path, "r") as f:
                self.assertIn("entry_points", f.read())
            self.assertIn(
                "cli.py",
                [f.name for f in (result.project / "batsay").iterdir()],
            )

    def test_bake_with_no_github_actions(self):
        with common.bake_in_temp_dir(
            self.cookies, extra_context={"github_actions": "n"}
        ) as result:
            self.assertNotIn(
                ".github", [f.name for f in result.project.iterdir()],
            )


if __name__ == "__main__":
    unittest.main()
