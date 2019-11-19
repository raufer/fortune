from user_agent import generate_user_agent


def user_agent() -> str:
    """
    A user agent is a string that a browser or app sends to each
    website you visit. A typical user agent string contains details
    like:
    - the application type,
    - operating system,
    - software vendor or software version of the requesting software user agent.

    Every request made from a web browser contains a user-agent header.
    When scraping many pages from a website, using the same user-agent
    consistently leads to the detection of a scraper.

    A way to bypass that detection is by faking your user agent and
    changing it with every request you make to a website.
    """
    return generate_user_agent()