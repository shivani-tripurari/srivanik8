import json
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for, request, jsonify
import requests

data=[{'title': 'Lesbian, gay and bisexual people far less likely to be religious', 'url': 'https://www.thetimes.co.uk/article/lesbian-gay-and-bisexual-people-far-less-likely-to-be-religious-75jjhrn5m', 'source': 'thetimes-lesbian'}, {'title': 'Lesbian Love Story by Amelia Possanza review — lesbians who redefined love', 'url': 'https://www.thetimes.co.uk/article/lesbian-love-story-by-amelia-possanza-review-lesbians-who-redefined-love-35v2kmp5d', 'source': 'thetimes-lesbian'}, {'title': 'Macron advisers wanted PM to come out as lesbian, book claims', 'url': 'https://www.thetimes.co.uk/article/macron-advisers-wanted-pm-to-come-out-as-lesbian-book-claims-f6sjldhrz', 'source': 'thetimes-lesbian'}, {'title': 'It’s a tough fight, but I’m backing the lesbians', 'url': 'https://www.thetimes.co.uk/article/its-a-tough-fight-but-im-backing-the-lesbians-v5cgkd0hv', 'source': 'thetimes-lesbian'}, {'title': 'Gender reform bill has betrayed lesbians — and will send them back into the closet', 'url': 'https://www.thetimes.co.uk/article/gender-reform-bill-has-betrayed-lesbians-and-will-send-them-back-into-the-closet-2x3rtd509', 'source': 'thetimes-lesbian'}, {'title': '‘I’m offended by Tár as a woman, as a conductor, as a lesbian’', 'url': 'https://www.thetimes.co.uk/article/im-offended-by-tar-as-a-woman-as-a-conductor-as-a-lesbian-t22vg7p70', 'source': 'thetimes-lesbian'}, {'title': 'Street preacher was charged with hate crime for quoting Bible at lesbians', 'url': 'https://www.thetimes.co.uk/article/street-preacher-was-charged-with-hate-crime-for-quoting-bible-at-lesbians-xbrhgr25r', 'source': 'thetimes-lesbian'}, {'title': 'Woman whose boss asked ‘how do lesbians have sex’ wins £30,000 award', 'url': 'https://www.thetimes.co.uk/article/woman-whose-boss-asked-how-do-lesbians-have-sex-wins-30-000-award-dcnh9s0d5', 'source': 'thetimes-lesbian'}, {'title': 'The Faggots and Their Friends Between Revolutions review — life in a gay commune', 'url': 'https://www.thetimes.co.uk/article/the-faggots-and-their-friends-between-revolutions-review-life-in-a-gay-commune-2tbj7zlm8', 'source': 'thetimes-gay'}, {'title': 'Wes Streeting: I was torn between being gay and Christian', 'url': 'https://www.thetimes.co.uk/article/wes-streeting-i-was-torn-between-being-gay-and-christian-893zqvnz6', 'source': 'thetimes-gay'}, {'title': '‘Discrimination doesn’t exist in Russia, because you don’t talk about being gay’', 'url': 'https://www.thetimes.co.uk/article/discrimination-doesnt-exist-in-russia-because-you-dont-talk-about-being-gay-vfz9gl339', 'source': 'thetimes-gay'}, {'title': 'Progress flag is a symbol of ideology, not gay pride', 'url': 'https://www.thetimes.co.uk/article/progress-flag-is-a-symbol-of-ideology-not-gay-pride-0wkrhr3gq', 'source': 'thetimes-gay'}, {'title': '‘Being gay is not illegal in Turkey — but we are targeted every day’', 'url': 'https://www.thetimes.co.uk/article/homosexuality-not-illegal-we-are-targeted-every-day-in-istanbul-mfd806zp0', 'source': 'thetimes-gay'}, {'title': 'Jay Shetty: ‘When I became a monk, my mates thought I was gay’', 'url': 'https://www.thetimes.co.uk/article/jay-shetty-i-dont-believe-i-have-all-the-answers-tbmx6t36z', 'source': 'thetimes-gay'}, {'title': 'Pardons for historical gay crimes to be widened', 'url': 'https://www.thetimes.co.uk/article/pardons-for-historical-gay-crimes-to-be-widened-r7hzh9bfb', 'source': 'thetimes-gay'}, {'title': 'I felt like the only gay in the village before coming out, says loneliness minister', 'url': 'https://www.thetimes.co.uk/article/stuart-andrew-it-wasn-t-easy-to-admit-i-was-lonely-zn0pl86jg', 'source': 'thetimes-gay'}, {'title': 'Archbishop of Canterbury condemns Uganda over new anti-gay laws', 'url': 'https://www.thetimes.co.uk/article/archbishop-of-canterbury-condemns-uganda-anti-gay-laws-wbkwvqfm2', 'source': 'thetimes-gay'}, {'title': 'Progress flag is a symbol of ideology, not gay pride', 'url': 'https://www.thetimes.co.uk/article/progress-flag-is-a-symbol-of-ideology-not-gay-pride-0wkrhr3gq', 'source': 'thetimes-gay'}, {'title': 'Civil servants ‘must be free to question transgender identity’', 'url': 'https://www.thetimes.co.uk/article/civil-service-transgender-identity-women-workplace-trans-guidance-kzvgtlzbz', 'source': 'thetimes-transgender'}, {'title': 'Church of England appoints first transgender archdeacon', 'url': 'https://www.thetimes.co.uk/article/church-of-england-appoints-first-transgender-archdeacon-tl8l7fwz7', 'source': 'thetimes-transgender'}, {'title': 'Teacher faces remortgaging home to pay costs of transgender pupil row', 'url': 'https://www.thetimes.co.uk/article/teacher-faces-remortgaging-home-to-pay-costs-of-transgender-pupil-row-shh3nb3vl', 'source': 'thetimes-transgender'}, {'title': 'Bud Light loses top spot after transgender furore', 'url': 'https://www.thetimes.co.uk/article/bud-light-loses-top-spot-after-transgender-furore-x7j6r59fr', 'source': 'thetimes-transgender'}, {'title': 'Swim Ireland dives into diversity with transgender consultation', 'url': 'https://www.thetimes.co.uk/article/swim-ireland-dives-into-diversity-transgender-consultation-ssw5b7mwc', 'source': 'thetimes-transgender'}, {'title': 'Anger at transgender handbook for children in care', 'url': 'https://www.thetimes.co.uk/article/anger-at-transgender-handbook-for-children-in-care-wvb9gtgn9', 'source': 'thetimes-transgender'}, {'title': 'British Cycling considers banning transgender riders from elite women’s races', 'url': 'https://www.thetimes.co.uk/article/british-cycling-considers-banning-transgender-riders-from-elite-womens-races-52nzls5l5', 'source': 'thetimes-transgender'}, {'title': 'Austin Killips: transgender cyclist’s win renews criticism of rules', 'url': 'https://www.thetimes.co.uk/article/austin-killips-transgender-cyclist-s-win-prompts-fresh-criticism-vhwcvp9ls', 'source': 'thetimes-transgender'}, {'title': 'Equalpride Announces Support of Kevin Aviance’s CVNTY Ball Tour', 'url': 'https://www.advocate.comhttps://www.advocate.com/music/kevin-aviance-cvnty-ball-tour', 'source': 'advocate'}, {'title': "Legitimacy of 'customer' in Supreme Court gay rights case raises ethical and legal flags", 'url': 'https://abcnews.go.com/US/wireStory/legitimacy-customer-supreme-court-gay-rights-case-raises-100630620', 'source': 'abcnews'}, {'title': 'New lesbian bars spark hope amid disappearing LGBTQ+ spaces', 'url': 'https://abcnews.go.com/US/new-lesbian-bars-spark-hope-amid-disappearing-lgbtq/story?id=100045956', 'source': 'abcnews'}, {'title': 'Spotlight on lesbian bars and the importance of community', 'url': 'https://abcnews.go.com/US/video/spotlight-lesbian-bars-importance-community-100395969', 'source': 'abcnews'}, {'title': 'Russian lawmakers move to further restrict transgender rights in new legislation', 'url': 'https://abcnews.go.com/International/wireStory/russian-lawmakers-move-restrict-transgender-rights-new-legislation-101209723', 'source': 'abcnews'}, {'title': 'Russia’s first transgender politician drops her run for governor due to anti-LGBTQ+ bill', 'url': 'https://abcnews.go.com/International/wireStory/russias-transgender-politician-abandons-plans-run-governor-amid-101010637', 'source': 'abcnews'}, {'title': 'Tennessee can enforce ban on transgender care for minors, court says', 'url': 'https://abcnews.go.com/Health/wireStory/tennessee-enforce-ban-transgender-care-minors-now-court-100895512', 'source': 'abcnews'}, {'title': 'Sarah McBride vies to be the nation’s first openly transgender congressperson', 'url': 'https://abcnews.go.com/Politics/video/sarah-mcbride-vies-nations-openly-transgender-congressperson-100447749', 'source': 'abcnews'}, {'title': 'US judge lets Kentucky enforce ban on transgender youth care for now', 'url': 'https://www.reuters.com/article/kentucky-lgbt/us-judge-lets-kentucky-enforce-ban-on-transgender-youth-care-for-now-idUSKBN2YU1O1', 'source': 'reuters'}, {'title': "Toilet limits for transgender woman 'unacceptable' - Japan's top court", 'url': 'https://www.reuters.com/article/japan-lgbtq-toilet/toilet-limits-for-transgender-woman-unacceptable-japans-top-court-idUSKBN2YR0CR', 'source': 'reuters'}, {'title': 'Please Baby Please review — turgid and humourless queer cinema', 'url': 'https://www.thetimes.co.uk/article/please-baby-please-review-turgid-and-humourless-queer-cinema-f8nmtpj6r', 'source': 'thetimes-queer'}, {'title': 'Hedda Gabler review — Anna Popplewell compels in queer update', 'url': 'https://www.thetimes.co.uk/article/hedda-gabler-review-anna-popplewell-compels-in-queer-update-sv82m8p2g', 'source': 'thetimes-queer'}, {'title': 'Marcelino Sambé: ‘Why are there no queer ballets?’', 'url': 'https://www.thetimes.co.uk/article/marcelino-sambe-why-are-there-no-queer-ballets-93rjr3jhd', 'source': 'thetimes-queer'}, {'title': 'Tour takes pride in revealing queer history of the city', 'url': 'https://www.thetimes.co.uk/article/tour-takes-pride-in-revealing-queer-history-of-the-city-7klqmsftd', 'source': 'thetimes-queer'}, {'title': 'Billy Porter: ‘They told me my queerness would be a liability. They were right for decades until they were not’', 'url': 'https://www.thetimes.co.uk/article/billy-porter-they-told-me-my-queerness-would-be-a-liability-they-were-right-for-decades-until-they-were-not-vkczvfrh6', 'source': 'thetimes-queer'}, {'title': 'What ‘queer’ means now', 'url': 'https://www.thetimes.co.uk/article/what-queer-means-now-g6pc6l3dw', 'source': 'thetimes-queer'}, {'title': 'Tour takes pride in revealing queer history of the city', 'url': 'https://www.thetimes.co.uk/article/tour-takes-pride-in-revealing-queer-history-of-the-city-7klqmsftd', 'source': 'thetimes-queer'}, {'title': 'His Sexuality Doesn’t Define Him, but It Can Set Him ApartEric Bach is an openly gay broadcaster for the Fredericksburg Nationals. He has major league aspirations, but his path has been much lonelier than he would prefer.By Zach BuchananPRINT EDITIONA Gay Broadcaster Climbs the Ladder, But It’s Been Lonely|2023-07-16T00:00:00-04:00, Page A27', 'url': 'https://www.nytimes.com/2023/07/15/sports/baseball/eric-bach-gay-baseball-announcer.html?searchResultPosition=1', 'source': 'nytimes-lgbt'}, {'title': 'My Fetish for a Second SkinAs a gay Korean American, I yearned for the privilege of being heterosexual or white. So I began wearing latex, a new skin.By Preston Gyuwon SoPRINT EDITIONA Pathway Toward Appreciating His Skins|2023-07-16T00:00:00-04:00, Page ST5', 'url': 'https://www.nytimes.com/2023/07/14/style/modern-love-latex-fetish-second-skin.html?searchResultPosition=3', 'source': 'nytimes-lgbt'}, {'title': '‘It’s my Florida too’: Pulse shooting survivor Brandon Wolf on being Black, gay and the anti-Ron DeSantis', 'url': 'https://www.theguardian.com/us-news/2023/jul/14/brandon-wolf-florida-desantis-lgbtq-gun-safety', 'source': 'theguardian'}, {'title': '‘It’s my Florida too’: Pulse shooting survivor Brandon Wolf on being Black, gay and the anti-Ron DeSantis', 'url': 'https://www.theguardian.com/us-news/2023/jul/14/brandon-wolf-florida-desantis-lgbtq-gun-safety', 'source': 'theguardian'}, {'title': 'Rediscovering India’s lost queer icons: a tour of Old Delhi’s secret history', 'url': 'https://www.theguardian.com/global-development/2023/jul/10/lgbtqi-identity-india-walking-tour-reclaiming-lost-queer-history-delhi', 'source': 'theguardian'}, {'title': 'Rediscovering India’s lost queer icons: a tour of Old Delhi’s secret history', 'url': 'https://www.theguardian.com/global-development/2023/jul/10/lgbtqi-identity-india-walking-tour-reclaiming-lost-queer-history-delhi', 'source': 'theguardian'}, {'title': 'Wolves first club to be punished by FA solely for homophobic chant', 'url': 'https://www.theguardian.com/football/2023/jul/14/wolves-fa-football-homophobic-chanting-chelsea', 'source': 'theguardian'}, {'title': 'Wolves first club to be punished by FA solely for homophobic chant', 'url': 'https://www.theguardian.com/football/2023/jul/14/wolves-fa-football-homophobic-chanting-chelsea', 'source': 'theguardian'}, {'title': 'Dominican theologian to German Bishop Bätzing: Support for gay agenda is ‘modernist heresy’', 'url': 'https://www.catholicnewsagency.com/news/252887/dominican-theologian-to-german-bishop-batzing-support-for-gay-agenda-is-modernist-heresy', 'source': 'catholicnewsagency'}, {'title': 'Tennessee governor urges investigation of Vanderbilt pediatric transgender clinic', 'url': 'https://www.catholicnewsagency.com/news/252356/tennessee-governor-urges-investigation-of-vanderbilt-pediatric-transgender-clinic', 'source': 'catholicnewsagency'}, {'title': 'Professor who resisted mandatory transgender pronouns reaches settlement with university', 'url': 'https://www.catholicnewsagency.com/news/251013/after-challenge-to-mandatory-transgender-pronouns-shawnee-state-university-reaches-settlement-with-professor-nicholas-meriwether', 'source': 'catholicnewsagency'}, {'title': "Latvia swears in EU's first openly gay president", 'url': 'https://www.bbc.com//news/world-europe-66141706', 'source': 'bbc.com-lgbt'}, {'title': 'What does transgender mean and what does the law say?', 'url': 'https://www.bbc.com//news/explainers-53154286', 'source': 'bbc.com-lgbt'}, {'title': 'Teen released after trans pride event pellet attack', 'url': 'https://www.bbc.com//news/uk-england-bristol-66121154', 'source': 'bbc.com-lgbt'}, {'title': "Ivo Dimchev: gay singer/songwriter's Bulgarian rhapsodies", 'url': '/story.php?ch=bartab&sc=live_music&id=326459', 'source': 'ebar'}, {'title': 'Fate of gay bathhouse chain Steamworks hangs in balance amid ongoing legal fight', 'url': '/story.php?ch=bartab&sc=sexuality&id=326338', 'source': 'ebar'}, {'title': "Extensive Castro Street closure OK'd, but panel nixes lesbian tech confab takeover of Warner plaza", 'url': '/story.php?ch=News&sc=News&id=326858', 'source': 'ebar'}, {'title': 'News Briefs: Interactive queer health exhibit launches in South Bay', 'url': '/story.php?ch=news&sc=news&id=326805', 'source': 'ebar'}, {'title': "'Hi Honey, I'm Homo!' — new book traces the history of queers on sitcoms", 'url': '/story.php?ch=arts__culture&sc=books&id=326736', 'source': 'ebar'}, {'title': "Drag performers of color reflect on 'queer joy' — and the current backlash to their art", 'url': '/story.php?ch=bartab&sc=drag&id=326263', 'source': 'ebar'}, {'title': 'Istanbul gay pride activists rally despite ban', 'url': 'https://www.euronews.com/2023/06/25/istanbul-gay-pride-activists-rally-despite-ban', 'source': 'euronews'}, {'title': "Turkish activists on Sunday defied a ban to stage an annual gay pride march in Istanbul one month after Turkey's election followed a homophobic hate-filled campaign.", 'url': 'https://www.euronews.com/2023/06/25/istanbul-gay-pride-activists-rally-despite-ban', 'source': 'euronews'}, {'title': 'Travelling the world isn’t easy when you’re gay. Here’s my experience', 'url': 'https://www.euronews.com/travel/2023/06/06/where-love-is-illegal-what-its-really-like-travelling-sri-lanka-as-a-gay-couple', 'source': 'euronews'}, {'title': "Sri Lanka is yet to decriminalise same-sex relationships. Here's how we navigated the country as a gay couple.", 'url': 'https://www.euronews.com/travel/2023/06/06/where-love-is-illegal-what-its-really-like-travelling-sri-lanka-as-a-gay-couple', 'source': 'euronews'}, {'title': "Gay Days will see LGBTQ+ celebrations at Disney and venues across Orlando in the midst of Governor Ron DeSantis' sweeping anti-gay legislation", 'url': 'https://www.euronews.com/culture/2023/06/02/lgbtq-community-parties-in-florida-amid-controversial-legislation', 'source': 'euronews'}, {'title': 'They warn that newly passed laws and policies may pose risks to minorities, immigrants and gay travellers.', 'url': 'https://www.euronews.com/travel/2023/05/24/florida-travel-warning-issued-by-civil-rights-groups-in-wake-of-hostile-laws', 'source': 'euronews'}, {'title': "Many claim the assault on a Brazilian transgender woman in Milan is yet another case of discrimination - set against the anti-LGBT+ rhetoric of Meloni's government.", 'url': 'https://www.euronews.com/2023/05/26/italian-governments-anti-lgbt-rhetoric-blamed-for-brutal-beating-of-trans-woman-in-milan', 'source': 'euronews'}, {'title': 'Rachel Pollack was a pioneering trans activist, authority on tarot and the occult and created the first transgender superhero in mainstream comics, Kate Godwin', 'url': 'https://www.euronews.com/culture/2023/04/10/writer-and-trans-activist-rachel-pollack-dies-aged-77', 'source': 'euronews'}, {'title': "Spain's new 'transgender' law breaks new ground on LGBTIQ+ rights", 'url': 'https://www.euronews.com/2023/04/06/how-spains-transgender-law-is-changing-the-lives-of-those-affected', 'source': 'euronews'}, {'title': 'Istanbul gay pride activists rally despite ban', 'url': 'https://www.euronews.com/2023/06/25/istanbul-gay-pride-activists-rally-despite-ban', 'source': 'euronews'}, {'title': "Turkish activists on Sunday defied a ban to stage an annual gay pride march in Istanbul one month after Turkey's election followed a homophobic hate-filled campaign.", 'url': 'https://www.euronews.com/2023/06/25/istanbul-gay-pride-activists-rally-despite-ban', 'source': 'euronews'}, {'title': "Turkish activists on Sunday defied a ban to stage an annual gay pride march in Istanbul one month after Turkey's election followed a homophobic hate-filled campaign.", 'url': 'https://www.euronews.com/2023/06/25/istanbul-gay-pride-activists-rally-despite-ban', 'source': 'euronews'}, {'title': 'Countries that have decriminalised homosexuality have 4.5 times higher rates of foreign direct investment (FDI) than countries that criminalise consensual same-sex relationships, M V Lee Badgett writes.', 'url': 'https://www.euronews.com/2023/05/17/uzbekistan-needs-a-new-economic-approach-that-includes-the-lgbtq-community', 'source': 'euronews'}]

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")


oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)


# Controllers API
@app.route("/")
def home():
    return render_template(
        "home.html",
        session=session.get("user"),
        pretty=json.dumps(session.get("user"), indent=4),posts=data
    )


@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")


@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )

#@app.route('/dashboard')
#def dashboard():
 #   headers = {
  #      'X-RapidAPI-Host': 'lgbtq-world-news-live.p.rapidapi.com',
   #     'X-RapidAPI-Key': '171dbe7b5cmsh57e443ff1588948p1cf21ejsne7c90a289974' 
    #}
    #response = requests.get('https://lgbtq-world-news-live.p.rapidapi.com/news', headers=headers)
    #data = response.json()
    #print(data)
    #return render_template('dashboard.html',posts=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=env.get("PORT", 3000))