"""

This example demonstrates how to write a custom highlighter.

"""

import secrets

from rich import print
from rich.highlighter import Highlighter


class RainbowHighlighter(Highlighter):
    def highlight(self, text):
        for index in range(len(text)):
            text.stylize(
                f"color({secrets.SystemRandom().randint(16, 255)})", index, index + 1
            )


rainbow = RainbowHighlighter()
print(rainbow("I must not fear. Fear is the mind-killer."))
