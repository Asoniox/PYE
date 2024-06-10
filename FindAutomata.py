"""Find Automata v0.1"""

import webbrowser


def openTab(url: str, new: int = 0, autoraise: bool = True):
    """openTab
    ---
    Parameters:
        url `str`: URL to open
        new `int`: Whether to open in new browser window. 0 is false, 1 is true
        autoraise `bool`: Whether to raise the window.
    Returns:
        webbrowser.open()
    """
    try:
        webbrowser.open(url, new, autoraise)
        print(f"Opened tab: {url}")
    except webbrowser.Error as e:
        print(f"WebBrowser Error - {e}")


def main(urls: list = []):
    """main
    ---
    Parameters
        urls `list`: List of URLs to open
    Returns
        openTab() for every url in the list
    """
    if list != []:
        for url in urls:
            openTab(url)
    else:
        print("No URLs to open.")


urls = [
    "https://calendar.google.com/calendar/u/0/r",
    "https://calendar.google.com/calendar/u/0/r/tasks",
    "https://pomofocus.io/",
]

main(urls)
