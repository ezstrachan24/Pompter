"""
Arthor: Edward Strachan
program: Prompter.py
"""

from breezypythongui import EasyFrame

class PrompterBoxDemo(EasyFrame):
    
    def __init__(self):
        """Sets up the window and widget."""
        EasyFrame.__init__(self, title = "Prompter Box Demo", width = 300, height = 100)
        self.label = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")
        self.addButton(text = "Username", row = 1, column = 0, command = self.getUserName)
    def getUserName(self):
        text = self.prompterBox(title = "Input Dialog", promptString = "Your Username:")
        self.label["text"] = "Hi " + text + " If you hear scraping at the window, Its Me"

def main():
    PrompterBoxDemo().mainloop()
main()
