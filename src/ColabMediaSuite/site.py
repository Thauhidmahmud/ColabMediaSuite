
# from IPython.display import IFrame, display
# import urllib.request
# from urllib.parse import urlparse

# from ColabMediaSuite.logger import logger
# from ColabMediaSuite.custom_exception import InvalidURLException


# def is_valid(url: str) -> bool:
#     try:
#         parsed = urlparse(url)

#         if parsed.scheme not in ["http", "https"]:
#             return False

#         urllib.request.urlopen(url, timeout=3).getcode()
#         return True

#     except Exception:
#         return False


# def render_site(url: str, width: str = "100%", height: str = "600"):
#     if not is_valid(url):
#         logger.error(f"Invalid URL: {url}")
#         raise InvalidURLException("The provided URL is invalid.")

#     logger.info(f"Valid URL: {url}")

#     display(IFrame(src=url, width=width, height=height))

#     return None   # IMPORTANT: no IPython object leak