from flask import Flask, render_template,jsonify
from flask_cors import CORS
from instagramy import InstagramUser
import json

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/works")
def it_works():
    return "IT Works!"

@app.route('/data/<usrname>')
def data(usrname):
    user = " "
    # usrname = "cretivox"
    print(usrname)
    # session_ig = ["48420109999%3AwYTofPNHOHFmPo%3A15%3AAYdePiWOn0bg3xhjxthCXGZ4ogwQzl2hbuT-QFLjbw" , "51669758945%3AQXe1CxsKaeEl0Z%3A14%3AAYcitzOLUpfaaC582rAfRbhWnz_5QSUIPnSNdhQYOQ"]
    session_id = "51669758945%3AeaoE7wCFnfMUUz%3A20%3AAYeauCt70M82lH0aKr9c-h3ZnUmHS5lgY6fKsNQGyw"
    # session_id = "55477599603%3Aw3s91KvLntecX2%3A18%3AAYdEgP1TpmPoe0mBTuzkaxdhF28IwVIxKWh28KCWPA"
    try:
        user = InstagramUser(usrname, sessionid=session_id)
        print("user : ", user)
    except:
        print("user : ", user)
        return render_template("index.html")
    user = InstagramUser(usrname, sessionid=session_id)
    ig_user = user.fullname
    follower = user.number_of_followers
    Photo = user.profile_picture_url
    verified = user.is_verified
    print(user.number_of_followers)
    print(user.profile_picture_url)
    data = user.user_data
    # print(len(data["edge_owner_to_timeline_media"]["edges"]))
    total_num_likes = 0
    total_num_comments = 0
    for i in range(len(data["edge_owner_to_timeline_media"]["edges"])):
        total_num_likes += int(data["edge_owner_to_timeline_media"]["edges"][i]["node"]["edge_liked_by"]["count"])
        total_num_comments += int(data["edge_owner_to_timeline_media"]["edges"][i]["node"]["edge_media_to_comment"]["count"])
    # print("total comment : " + str(total_num_comments))
    # print("total like : " + str(total_num_likes))
    value = float(total_num_comments/12) + float(total_num_likes/12)
    ER_account = (value / user.number_of_followers) * 100
    # print(ER_account)
    # with open('data.json', 'w') as outfile:
    #     json.dump(data, outfile)
    if(len(data["edge_related_profiles"]["edges"]) == 0):
        r1,r2,r3 = "Not Found","Not Found","Not Found"
    else:
        r1 = data["edge_related_profiles"]["edges"][0]["node"]["username"]
        r2 = data["edge_related_profiles"]["edges"][1]["node"]["username"]
        r3 = data["edge_related_profiles"]["edges"][2]["node"]["username"]
    # print(len(data["edge_related_profiles"]["edges"]))
    # print(data["edge_related_profiles"]["edges"][0]["node"]["username"])
    jsondat = [
        {
        "status": 200,
        "username": usrname,
        "name" : ig_user,
        "follower" : follower,
        "url" : "https://floral-dream-d6be.cretivox-dev.workers.dev/" + Photo,
        "verified": verified,
        "er": ER_account,
        "r1": r1,
        "r2": r2,
        "r3": r3,
    }
    ]
    return jsonify(jsondat)
