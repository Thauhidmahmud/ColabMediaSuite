# from IPython.display import YouTubeVideo
# from ColabMediaSuite.logger import logger


# def safe_display(obj):
#     try:
#         from IPython.display import display
#         display(obj)
#     except Exception:
#         print(obj)


# def render_youtube_video(url: str):
#     try:
#         video_id = url.split("v=")[-1].split("&")[0]

#         logger.info(f"Rendering YouTube video: {url}")

#         safe_display(YouTubeVideo(video_id))

#         return "success"

#     except Exception as e:
#         logger.error(f"Error: {e}")
#         return None