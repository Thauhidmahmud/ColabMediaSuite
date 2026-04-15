
# from ColabMediaSuite.site import render_site
# from ColabMediaSuite.youtube import render_youtube_video
from ColabMediaSuite.logger import logger
from ColabMediaSuite.custom_exception import InvalidURLException
# from ColabMediaSuite.site import render_site

try:
    raise InvalidURLException()

except Exception as e:
    logger.error(f"An error occurred: {e}")
