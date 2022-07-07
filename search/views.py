import requests
from isodate import parse_duration
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from api_keys.models import APIKeys


videos = []


def index(request):

    if request.method == "POST":
        search_url = "https://www.googleapis.com/youtube/v3/search"
        video_url = "https://www.googleapis.com/youtube/v3/videos"
        # change id to change api key
        key = APIKeys.objects.get(id=1)
        search_params = {
            "part": "snippet",
            "q": request.POST["search"],
            "key": str(key),
            "maxResults": 45,
            "type": "video",
            "order": "relevance",
            #'publishedAfter' : 'datetime',
        }

        r = requests.get(search_url, params=search_params)

        results = r.json()["items"]

        video_ids = []
        for result in results:
            video_ids.append(result["id"]["videoId"])

        if request.POST["submit"] == "lucky":
            return redirect(f"https://www.youtube.com/watch?v={ video_ids[0] }")

        video_params = {
            "key": str(key),
            "part": "snippet,contentDetails",
            "id": ",".join(video_ids),
            "maxResults": 45,
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()["items"]

        for result in results:
            video_data = {
                "title": result["snippet"]["title"],
                "id": result["id"],
                "url": f'https://www.youtube.com/watch?v={ result["id"] }',
                "duration": int(
                    parse_duration(result["contentDetails"]["duration"]).total_seconds()
                    // 60
                ),
                "thumbnail": result["snippet"]["thumbnails"]["high"]["url"],
            }

            videos.append(video_data)
    page = request.GET.get("page", 1)

    paginator = Paginator(videos, 9)
    try:
        vids = paginator.page(page)
    except PageNotAnInteger:
        vids = paginator.page(1)
    except EmptyPage:
        vids = paginator.page(paginator.num_pages)
    return render(request, "search/index.html", {"vids": vids})
