import os, json, glob
exec(open(ADAPT).read())
T = {}
def _rec(fn):
    def w(name, *a, **k):
        p = name.split("_")[0]
        if p not in T:
            T[p] = a[1] if fn.__name__ in ("cover", "single", "cards") else a[0]
        return fn(name, *a, **k)
    w.__name__ = fn.__name__; return w
cover, single, cards = _rec(cover), _rec(single), _rec(cards)
exec(open(BODY + "/month_body.py").read())
for p in ("1130", "1207", "1208"):
    for x in glob.glob(f"{OUT}/{p}*.jpg"): os.remove(x)
    T.pop(p, None)
exec(open(BODY + "/repl_body.py").read())
exec(open(BODY + "/dec_body.py").read())
exec(open(BODY + "/caps_w24.py").read())
CAP.update(CAP2); CAP.update(CAP3)
NEW = {"2026-11-30", "2026-12-07", "2026-12-08"}
PLAN = {}
for d, (p, c) in sorted(CAP.items()):
    fs = sorted(os.path.basename(x) for x in glob.glob(f"{OUT}/{p}*.jpg") if os.path.basename(x).split("_")[0].split(".")[0] == p)
    PLAN[d] = {"topic": T.get(p, p), "files": ["posts/" + x for x in fs], "caption": c,
               "status": "skip" if d in NEW else "pending"}
json.dump(PLAN, open(BODY + "/plan_rest.json", "w"), indent=1, ensure_ascii=False)
print(len(PLAN), sum(len(v["files"]) for v in PLAN.values()))
