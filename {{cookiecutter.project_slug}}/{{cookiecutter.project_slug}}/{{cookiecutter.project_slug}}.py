BAT = """
                    {message}
                     /
    =/\\             /   /\\=
    / \\'._   (\\_/) / _.'/ \\
   / .''._'--(o.o)--'_.''. \\
  /.' _/ |`'=/ " \\='`| \\_ `.\\
 /` .' `\\;-,'\\___/',-;/` '. '\\
/.-'       `\\(-V-)/`       `-.\\
`            "   "
(tm)
"""


def say(message):
    """
    Say a message.

    Paramaters
    ----------
    message: str
      Message to say.

    Returns
    -------
    str
      Sayed message.
    """
    r = BAT.format(message=message)
    return r
