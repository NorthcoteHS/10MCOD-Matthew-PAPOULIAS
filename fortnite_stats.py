import urllib.request
import json
import sys

def parse_args():
    return sys.argv[1], sys.argv[2]

def create_url(name, platform):
    url = "https://api.fortnitetracker.com/v1/profile/" + platform + "/" + name
    return url

def create_request(url, api_key, agent):
    header = {"TRN-Api-Key": api_key, "User-Agent": agent}
    req = urllib.request.Request(url, headers=header)
    return req

def send_request(req):
    return urllib.request.urlopen(req)

def parse_resp(resp):
    parsed = json.loads(resp)
    print("\n{platform} - {user}:\n".format(user=parsed["epicUserHandle"], platform=parsed["platformNameLong"]))
    print("Solo:")
    print("Wins - {}".format(parsed["stats"]["p2"]["top1"]["value"]))
    print("Top 10 - {}".format(parsed["stats"]["p2"]["top10"]["value"]))
    print("Top 25 - {}".format(parsed["stats"]["p2"]["top25"]["value"]))
    print("Kills - {}".format(parsed["stats"]["p2"]["kills"]["value"]))
    print("K/D - {}".format(parsed["stats"]["p2"]["kd"]["value"]))
    print("Kills per Match - {}".format(parsed["stats"]["p2"]["kpg"]["value"]))
    try:
        print("Win Chance - {}%".format(parsed["stats"]["p2"]["winRatio"]["value"]))
    except:
        print("Win Chance - 0.00%")

    print("\nDuo:")
    print("Wins - {}".format(parsed["stats"]["p10"]["top1"]["value"]))
    print("Top 10 - {}".format(parsed["stats"]["p10"]["top5"]["value"]))
    print("Top 25 - {}".format(parsed["stats"]["p10"]["top12"]["value"]))
    print("Kills - {}".format(parsed["stats"]["p10"]["kills"]["value"]))
    print("K/D - {}".format(parsed["stats"]["p10"]["kd"]["value"]))
    print("Kills per Match - {}".format(parsed["stats"]["p10"]["kpg"]["value"]))
    try:
        print("Win Chance - {}%".format(parsed["stats"]["p10"]["winRatio"]["value"]))
    except:
        print("Win Chance - 0.00%")

    print("\nSquad:")
    print("Wins - {}".format(parsed["stats"]["p9"]["top1"]["value"]))
    print("Top 10 - {}".format(parsed["stats"]["p9"]["top3"]["value"]))
    print("Top 25 - {}".format(parsed["stats"]["p9"]["top6"]["value"]))
    print("Kills - {}".format(parsed["stats"]["p9"]["kills"]["value"]))
    print("K/D - {}".format(parsed["stats"]["p9"]["kd"]["value"]))
    print("Kills per Match - {}".format(parsed["stats"]["p9"]["kpg"]["value"]))
    try:
        print("Win Chance - {}%".format(parsed["stats"]["p9"]["winRatio"]["value"]))
    except:
        print("Win Chance - 0.00%")

if len(sys.argv) == 3:
    user, platform = parse_args()
elif len(sys.argv) > 1 and len(sys.argv) != 3:
    print("\nUsage:")
    print("python fortnite_stats.py <fortnite username> <platform>\n")
    sys.exit()
else:
    user = input("Enter fortnite username: ")
    platform = input("Enter platform (pc, xbox, ps4): ")

api_key = "01a383d1-7d81-4b7c-90e5-c71bba78d840"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
url = create_url(user, platform)
request = create_request(url, api_key, user_agent)
resp = send_request(request)
parse_resp(resp.read())
input("\nPress any key to continue...")
