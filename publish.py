import json, time, base64, urllib.request
REPO = "yagneshster-coder/rcmaxis-ig"
RAW = f"https://raw.githubusercontent.com/{REPO}/main/"
IG = "40181938194785489"

def _plan():
    r, e = run_composio_tool("GITHUB_GET_REPOSITORY_CONTENT", {"owner": REPO.split("/")[0], "repo": REPO.split("/")[1], "path": "plan.json", "ref": "main"})
    if e: raise RuntimeError(e)
    d = r.get("data", {}); c = d.get("content", d)
    c = c.get("content") if isinstance(c, dict) else c
    return json.loads(base64.b64decode(c.replace("\n", "")).decode())

def _id(r):
    d = (r or {}).get("data") or {}
    return d.get("id") or (d.get("data") or {}).get("id")

def publish_day(date, dry=False):
    P = _plan(); e = P.get(date)
    if not e: return {"date": date, "status": "missing"}
    if e.get("status") == "skip": return {"date": date, "status": "skip"}
    urls = [RAW + f for f in e["files"]]
    for u in urls:
        with urllib.request.urlopen(u, timeout=30) as resp:
            assert resp.status == 200 and resp.headers.get("Content-Type", "").startswith("image/"), u
    if dry: return {"date": date, "topic": e["topic"], "urls": urls, "dry": True}
    cap = e["caption"]
    if len(urls) == 1:
        r, err = run_composio_tool("INSTAGRAM_POST_IG_USER_MEDIA", {"ig_user_id": IG, "image_url": urls[0], "caption": cap})
        if err: raise RuntimeError(err)
        cid = _id(r)
    else:
        kids = []
        for u in urls:
            r, err = run_composio_tool("INSTAGRAM_POST_IG_USER_MEDIA", {"ig_user_id": IG, "image_url": u, "is_carousel_item": True})
            if err: raise RuntimeError(err)
            kids.append(_id(r)); time.sleep(2)
        r, err = run_composio_tool("INSTAGRAM_CREATE_CAROUSEL_CONTAINER", {"ig_user_id": IG, "children": kids, "caption": cap})
        if err: raise RuntimeError(err)
        cid = _id(r)
    r, err = run_composio_tool("INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH", {"ig_user_id": IG, "creation_id": cid, "max_wait_seconds": 120})
    if err: raise RuntimeError(err)
    mid = _id(r) or ((r or {}).get("data") or {}).get("ig_media_id")
    m, _ = run_composio_tool("INSTAGRAM_GET_IG_MEDIA", {"ig_media_id": mid, "fields": "id,permalink,caption"})
    md = (m or {}).get("data") or {}
    capd = md.get("caption") or ""
    return {"date": date, "topic": e["topic"], "media_id": mid, "permalink": md.get("permalink"),
            "caption_ok": ("%23" not in capd) and capd.strip()[-20:] == cap.strip()[-20:]}
