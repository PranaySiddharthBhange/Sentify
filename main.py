import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from deep_translator import GoogleTranslator
from textblob import TextBlob

# Define the data

demo_data = [
{'created_at': 'Mon Jan 01 21:07:36 +0000 2022', 'text': 'What grow yard eye reason debate commercial. Behavior happy create draw wish recent research writer.\nCharacter institution expect grow.', 'user': {'screen_name': 'rodriguezcassandra', 'location': 'East Jonathanchester, Maine', 'followers_count': 742496}, 'place': {'country_code': 'DZ', 'place_type': 'city', 'full_name': 'Hillfort, Vermont'}, 'entities': {'hashtags': ['trade', 'them']}},
{'created_at': 'Mon Jan 01 21:07:36 +0000 2022', 'text': 'Of coach parent loss allow development. Future lot everybody technology.', 'user': {'screen_name': 'rgoodman', 'location': 'Kentland, Nebraska', 'followers_count': 909289}, 'place': {'country_code': 'SL', 'place_type': 'city', 'full_name': 'Johnside, West Virginia'}, 'entities': {'hashtags': ['his', 'know']}},
{'created_at': 'Mon Jan 01 21:07:36 +0000 2022', 'text': 'Figure instead and. Subject general camera become expect.\nSuddenly reduce important explain nor though out travel. Keep along myself together.', 'user': {'screen_name': 'mary36', 'location': 'Brandonside, Nebraska', 'followers_count': 39843}, 'place': {'country_code': 'TH', 'place_type': 'city', 'full_name': 'Jenniferborough, Missouri'}, 'entities': {'hashtags': ['why', 'camera']}},
{'created_at': 'Mon Jan 01 21:07:36 +0000 2022', 'text': 'Sort company light per. Likely thus lay suddenly American.\nSon about else business brother. Magazine budget want put upon risk.', 'user': {'screen_name': 'kelleyallison', 'location': 'East Sarah, Wisconsin', 'followers_count': 611906}, 'place': {'country_code': 'AU', 'place_type': 'city', 'full_name': 'West Amyhaven, Indiana'}, 'entities': {'hashtags': ['think', 'around']}},
{'created_at': 'Mon Jan 01 21:07:36 +0000 2022', 'text': 'Practice maintain trouble parent themselves. Pick discuss think this defense environmental.\nHuge situation during Republican.\nOfficer share how indicate down rather a. Old over effect key.', 'user': {'screen_name': 'owillis', 'location': 'Nicolemouth, Vermont', 'followers_count': 377608}, 'place': {'country_code': 'AT', 'place_type': 'city', 'full_name': 'New Nicoleburgh, Alaska'}, 'entities': {'hashtags': ['truth', 'then']}},
{'created_at': 'Mon Jan 01 21:07:36 +0000 2022', 'text': 'Determine sit quickly shake. Culture material find ten compare reach plan few. Each popular red claim him they model.', 'user': {'screen_name': 'thomasmichael', 'location': 'Millershire, New Jersey', 'followers_count': 575027}, 'place': {'country_code': 'DJ', 'place_type': 'city', 'full_name': 'Savannahmouth, Utah'}, 'entities': {'hashtags': ['hand', 'whether']}},
{'created_at': 'Mon Jan 07 21:07:36 +0000 2022', 'text': 'Indicate eight Mrs simple when push subject. Their human similar let arm voice art prevent. Rule drive attention pull.\nPolice environment she game recognize your half. Born chair program hair two.', 'user': {'screen_name': 'shanejuarez', 'location': 'Washingtonstad, Virginia', 'followers_count': 261018}, 'place': {'country_code': 'VA', 'place_type': 'city', 'full_name': 'South Hannah, Maryland'}, 'entities': {'hashtags': ['above', 'member']}},
{'created_at': 'Mon Jan 08 21:07:36 +0000 2022', 'text': 'Language whom help particular suffer central try environment.\nOwn other fear conference town word size energy. Say explain loss at send pressure.', 'user': {'screen_name': 'zwhitehead', 'location': 'Benjaminmouth, North Carolina', 'followers_count': 780426}, 'place': {'country_code': 'LK', 'place_type': 'city', 'full_name': 'Danafurt, Minnesota'}, 'entities': {'hashtags': ['professional', 'provide']}},
{'created_at': 'Mon Jan 09 21:07:36 +0000 2022', 'text': 'Bad such without short. Under modern both dog close nearly ask. Fire sister security career.\nGuy ever identify often. Debate against action whose contain politics. Tell artist only western although.', 'user': {'screen_name': 'joshuadavis', 'location': 'New Kyle, Arkansas', 'followers_count': 990821}, 'place': {'country_code': 'IR', 'place_type': 'city', 'full_name': 'Courtneyfurt, Maryland'}, 'entities': {'hashtags': ['suddenly', 'claim']}},
{'created_at': 'Mon Jan 10 21:07:36 +0000 2022', 'text': 'Call family strategy dark. Exactly writer office whether board everything sing. More crime pass feel edge Republican assume.', 'user': {'screen_name': 'sparker', 'location': 'West Susan, Alaska', 'followers_count': 414514}, 'place': {'country_code': 'BN', 'place_type': 'city', 'full_name': 'Rayside, Oklahoma'}, 'entities': {'hashtags': ['walk', 'court']}},
{'created_at': 'Wed Mar 11 19:28:45 +0000 2022', 'text': 'Establish again north seem small they. Heavy bed I strategy goal various. Break eye skill rule. President purpose visit.', 'user': {'screen_name': 'ashleynichols', 'location': 'Williamborough, California', 'followers_count': 180373}, 'place': {'country_code': 'IR', 'place_type': 'city', 'full_name': 'Justinport, Texas'}, 'entities': {'hashtags': ['way', 'leave']}},
{'created_at': 'Mon Dec 12 03:41:05 +0000 2022', 'text': 'Forward place front daughter pass four maybe doctor. Cup rest beautiful fund work little. Region true late.\nYour TV become agreement student. Put middle must.', 'user': {'screen_name': 'cduncan', 'location': 'West Garystad, Delaware', 'followers_count': 136342}, 'place': {'country_code': 'NE', 'place_type': 'city', 'full_name': 'Meganmouth, Nebraska'}, 'entities': {'hashtags': ['yard', 'raise']}},
{'created_at': 'Sat Jun 13 18:44:55 +0000 2022', 'text': 'Detail hour ok conference light. Else box we skill stage. Interview give daughter attack ago role.\nEnjoy realize difference stay feeling. Green rich expert.', 'user': {'screen_name': 'nataliesharp', 'location': 'Rodriguezbury, Maine', 'followers_count': 986185}, 'place': {'country_code': 'MY', 'place_type': 'city', 'full_name': 'West Laura, North Dakota'}, 'entities': {'hashtags': ['lawyer', 'college']}},
{'created_at': 'Fri Aug 14 03:17:10 +0000 2022', 'text': 'Factor around class ever well answer. Respond deal want ten. Interesting forward possible citizen on prevent.', 'user': {'screen_name': 'jjohnson', 'location': 'Denisestad, Oregon', 'followers_count': 587279}, 'place': {'country_code': 'PG', 'place_type': 'city', 'full_name': 'Hamiltonfort, Ohio'}, 'entities': {'hashtags': ['space', 'store']}},
{'created_at': 'Sun Mar 15 10:03:16 +0000 2022', 'text': 'Organization loss offer marriage another enough state Democrat. Account either night evidence step you discussion.\nCompare fine five rise. I ahead animal year.', 'user': {'screen_name': 'qhiggins', 'location': 'East Stephenfurt, New York', 'followers_count': 157890}, 'place': {'country_code': 'PS', 'place_type': 'city', 'full_name': 'Smithport, West Virginia'}, 'entities': {'hashtags': ['begin', 'international']}},
{'created_at': 'Fri Mar 16 09:50:57 +0000 2022', 'text': 'Mouth fire significant. Finish land speech example talk move increase.\nMoney tough medical fear why ever. Paper much three shake hold minute road. Forward sort drug account chair interest option.', 'user': {'screen_name': 'eric52', 'location': 'East Sarahborough, Mississippi', 'followers_count': 338662}, 'place': {'country_code': 'CM', 'place_type': 'city', 'full_name': 'Kennethberg, Washington'}, 'entities': {'hashtags': ['new', 'we']}},
{'created_at': 'Mon Apr 17 19:01:11 +0000 2022', 'text': 'Wall base believe over. Consumer push radio mention. Arm yeah other country air. Admit become central.\nKid program base arm trip customer goal.', 'user': {'screen_name': 'jameswatson', 'location': 'Henryberg, New Jersey', 'followers_count': 273275}, 'place': {'country_code': 'QA', 'place_type': 'city', 'full_name': 'Williamsonchester, Alaska'}, 'entities': {'hashtags': ['dark', 'add']}},
{'created_at': 'Mon Feb 18 23:18:58 +0000 2022', 'text': 'My power spring rich record cup. Way again least say trouble. Product energy mind five spend then executive.\nIt degree visit side eat. Spring great mention firm face down vote.', 'user': {'screen_name': 'bdavis', 'location': 'Rebekahborough, Wisconsin', 'followers_count': 258525}, 'place': {'country_code': 'DJ', 'place_type': 'city', 'full_name': 'Joseside, Missouri'}, 'entities': {'hashtags': ['nothing', 'protect']}},
{'created_at': 'Fri Mar 19 09:49:17 +0000 2022', 'text': 'Author east later event. Doctor fast condition house agent. Student read they.\nHis determine serious much. Of research certainly concern kind accept push. Dog note them catch somebody.', 'user': {'screen_name': 'hannah32', 'location': 'Lake Bethside, Virginia', 'followers_count': 606170}, 'place': {'country_code': 'UY', 'place_type': 'city', 'full_name': 'Port Tonyport, North Carolina'}, 'entities': {'hashtags': ['practice', 'maintain']}},
{'created_at': 'Wed Aug 20 06:05:48 +0000 2022', 'text': 'Industry lead Democrat president allow. Nothing long half grow argue detail specific reduce. Anything carry every up quality why feeling.', 'user': {'screen_name': 'zbrooks', 'location': 'East Cathyburgh, Kansas', 'followers_count': 348517}, 'place': {'country_code': 'PL', 'place_type': 'city', 'full_name': 'East Steven, Colorado'}, 'entities': {'hashtags': ['industry', 'character']}},
{'created_at': 'Fri Dec 21 05:47:39 +0000 2022', 'text': 'Less attack recently far less. Year chance keep.\nTax lawyer base for. Federal cup city cover. Before condition building.', 'user': {'screen_name': 'margaret36', 'location': 'Lake Michele, North Dakota', 'followers_count': 204832}, 'place': {'country_code': 'LK', 'place_type': 'city', 'full_name': 'South Kellyberg, Mississippi'}, 'entities': {'hashtags': ['before', 'field']}},
{'created_at': 'Sat Feb 22 16:40:50 +0000 2022', 'text': 'Other explain free put many child design. Red animal different. Mr give point safe debate public color.', 'user': {'screen_name': 'kmoore', 'location': 'Gabrielmouth, Kentucky', 'followers_count': 851379}, 'place': {'country_code': 'CO', 'place_type': 'city', 'full_name': 'Greenborough, California'}, 'entities': {'hashtags': ['under', 'black']}},
{'created_at': 'Wed May 23 23:18:50 +0000 2022', 'text': 'Successful clear maybe successful message. More foot Mrs agree attorney despite.\nMission light foot book leader opportunity author accept. Discussion go friend new involve.', 'user': {'screen_name': 'johnsonmichael', 'location': 'South Chad, South Carolina', 'followers_count': 320326}, 'place': {'country_code': 'VE', 'place_type': 'city', 'full_name': 'Lake Gregory, Montana'}, 'entities': {'hashtags': ['forward', 'where']}},
{'created_at': 'Wed Oct 24 09:59:20 +0000 2022', 'text': 'Product production lead best. Amount current research protect wrong. Environmental third suggest bill feeling shake indicate.', 'user': {'screen_name': 'reidronnie', 'location': 'West Robertview, Nevada', 'followers_count': 810607}, 'place': {'country_code': 'BH', 'place_type': 'city', 'full_name': 'Vanessaton, Nevada'}, 'entities': {'hashtags': ['and', 'yes']}},
{'created_at': 'Sat Jan 25 14:52:04 +0000 2022', 'text': 'Need hundred ready knowledge official attention receive. School fact nature toward skin prevent. Customer family step leader suggest focus perhaps.', 'user': {'screen_name': 'fcarrillo', 'location': 'Kevinstad, Wyoming', 'followers_count': 407769}, 'place': {'country_code': 'MZ', 'place_type': 'city', 'full_name': 'Michelleburgh, Nevada'}, 'entities': {'hashtags': ['hour', 'during']}},
{'created_at': 'Sun Oct 25 07:46:35 +0000 2022', 'text': 'Child when before author. Local employee wrong although try. Short fund police home adult quickly ready anyone.\nReport exactly meet set. Office prove picture trade age talk decide song.', 'user': {'screen_name': 'fitzpatrickmark', 'location': 'Bradberg, Delaware', 'followers_count': 239726}, 'place': {'country_code': 'TO', 'place_type': 'city', 'full_name': 'Cynthiamouth, Maryland'}, 'entities': {'hashtags': ['clear', 'month']}},
{'created_at': 'Tue Nov 27 02:03:10 +0000 2022', 'text': 'Customer bar too walk station. Wrong section alone yourself although. Worker keep result choose plan around.\nThose for very adult beyond. Must past in long above put wish.', 'user': {'screen_name': 'barnesamanda', 'location': 'Schneiderhaven, North Dakota', 'followers_count': 845099}, 'place': {'country_code': 'JO', 'place_type': 'city', 'full_name': 'Wolfemouth, New Hampshire'}, 'entities': {'hashtags': ['score', 'myself']}},
{'created_at': 'Sun Dec 28 15:30:11 +0000 2022', 'text': 'Professional nor century wall discuss. Perform common grow crime miss power necessary. Direction represent move ready significant.', 'user': {'screen_name': 'kwilliams', 'location': 'Patricktown, Nebraska', 'followers_count': 489862}, 'place': {'country_code': 'MW', 'place_type': 'city', 'full_name': 'Port Jeremy, North Carolina'}, 'entities': {'hashtags': ['operation', 'people']}},
{'created_at': 'Tue Sep 29 01:52:37 +0000 2022', 'text': 'Bit rest image keep. Candidate always along raise hope event. Behavior culture health.\nProject fact grow outside technology government home. Option pick face people.\nStory seat political oil.', 'user': {'screen_name': 'salassuzanne', 'location': 'West Andrea, Oklahoma', 'followers_count': 853662}, 'place': {'country_code': 'YE', 'place_type': 'city', 'full_name': 'Deannafurt, Kentucky'}, 'entities': {'hashtags': ['focus', 'herself']}},
{'created_at': 'Thu May 30 11:13:55 +0000 2022', 'text': 'Picture even teach radio fire. Image end certain boy off place film. On may sea support report big candidate act. Suddenly agree about whom fight make.', 'user': {'screen_name': 'carolyngillespie', 'location': 'Mcfarlandbury, Oklahoma', 'followers_count': 39189}, 'place': {'country_code': 'FJ', 'place_type': 'city', 'full_name': 'East Sandrahaven, Wisconsin'}, 'entities': {'hashtags': ['set', 'result']}},
{'created_at': 'Fri Dec 31 05:47:39 +0000 2022', 'text': 'Less attack recently far less. Year chance keep.\nTax lawyer base for. Federal cup city cover. Before condition building.', 'user': {'screen_name': 'margaret36', 'location': 'Lake Michele, North Dakota', 'followers_count': 204832}, 'place': {'country_code': 'LK', 'place_type': 'city', 'full_name': 'South Kellyberg, Mississippi'}, 'entities': {'hashtags': ['before', 'field']}},
{'created_at': 'Sat Feb 01 16:40:50 +0000 2022', 'text': 'Other explain free put many child design. Red animal different. Mr give point safe debate public color.', 'user': {'screen_name': 'kmoore', 'location': 'Gabrielmouth, Kentucky', 'followers_count': 851379}, 'place': {'country_code': 'CO', 'place_type': 'city', 'full_name': 'Greenborough, California'}, 'entities': {'hashtags': ['under', 'black']}},
{'created_at': 'Wed May 02 23:18:50 +0000 2022', 'text': 'Successful clear maybe successful message. More foot Mrs agree attorney despite.\nMission light foot book leader opportunity author accept. Discussion go friend new involve.', 'user': {'screen_name': 'johnsonmichael', 'location': 'South Chad, South Carolina', 'followers_count': 320326}, 'place': {'country_code': 'VE', 'place_type': 'city', 'full_name': 'Lake Gregory, Montana'}, 'entities': {'hashtags': ['forward', 'where']}},
{'created_at': 'Wed Oct 03 09:59:20 +0000 2022', 'text': 'Product production lead best. Amount current research protect wrong. Environmental third suggest bill feeling shake indicate.', 'user': {'screen_name': 'reidronnie', 'location': 'West Robertview, Nevada', 'followers_count': 810607}, 'place': {'country_code': 'BH', 'place_type': 'city', 'full_name': 'Vanessaton, Nevada'}, 'entities': {'hashtags': ['and', 'yes']}},
{'created_at': 'Sat Jan 04 14:52:04 +0000 2022', 'text': 'Need hundred ready knowledge official attention receive. School fact nature toward skin prevent. Customer family step leader suggest focus perhaps.', 'user': {'screen_name': 'fcarrillo', 'location': 'Kevinstad, Wyoming', 'followers_count': 407769}, 'place': {'country_code': 'MZ', 'place_type': 'city', 'full_name': 'Michelleburgh, Nevada'}, 'entities': {'hashtags': ['hour', 'during']}},
{'created_at': 'Sun Oct 05 07:46:35 +0000 2022', 'text': 'Child when before author. Local employee wrong although try. Short fund police home adult quickly ready anyone.\nReport exactly meet set. Office prove picture trade age talk decide song.', 'user': {'screen_name': 'fitzpatrickmark', 'location': 'Bradberg, Delaware', 'followers_count': 239726}, 'place': {'country_code': 'TO', 'place_type': 'city', 'full_name': 'Cynthiamouth, Maryland'}, 'entities': {'hashtags': ['clear', 'month']}},
{'created_at': 'Tue Nov 06 02:03:10 +0000 2022', 'text': 'Customer bar too walk station. Wrong section alone yourself although. Worker keep result choose plan around.\nThose for very adult beyond. Must past in long above put wish.', 'user': {'screen_name': 'barnesamanda', 'location': 'Schneiderhaven, North Dakota', 'followers_count': 845099}, 'place': {'country_code': 'JO', 'place_type': 'city', 'full_name': 'Wolfemouth, New Hampshire'}, 'entities': {'hashtags': ['score', 'myself']}},
{'created_at': 'Sun Jan 01 15:30:11 +0000 2022', 'text': 'Professional nor century wall discuss. Perform common grow crime miss power necessary. Direction represent move ready significant.', 'user': {'screen_name': 'kwilliams', 'location': 'Patricktown, Nebraska', 'followers_count': 489862}, 'place': {'country_code': 'MW', 'place_type': 'city', 'full_name': 'Port Jeremy, North Carolina'}, 'entities': {'hashtags': ['operation', 'people']}},
{'created_at': 'Tue Sep 08 01:52:37 +0000 2022', 'text': 'Bit rest image keep. Candidate always along raise hope event. Behavior culture health.\nProject fact grow outside technology government home. Option pick face people.\nStory seat political oil.', 'user': {'screen_name': 'salassuzanne', 'location': 'West Andrea, Oklahoma', 'followers_count': 853662}, 'place': {'country_code': 'YE', 'place_type': 'city', 'full_name': 'Deannafurt, Kentucky'}, 'entities': {'hashtags': ['focus', 'herself']}},
{'created_at': 'Thu May 09 11:13:55 +0000 2022', 'text': 'Picture even teach radio fire. Image end certain boy off place film. On may sea support report big candidate act. Suddenly agree about whom fight make.', 'user': {'screen_name': 'carolyngillespie', 'location': 'Mcfarlandbury, Oklahoma', 'followers_count': 39189}, 'place': {'country_code': 'FJ', 'place_type': 'city', 'full_name': 'East Sandrahaven, Wisconsin'}, 'entities': {'hashtags': ['set', 'result']}},

]


# Translate text function
def translate_text(text, source_lang="auto", target_lang="en"):
    return GoogleTranslator().translate(text, source=source_lang, target=target_lang)

# Sentiment analysis function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity

    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

# Filter data by hashtags function
def filter_data_by_hashtags(data, hashtags):
    filtered_data = []

    for tweet in data:
        tweet_hashtags = tweet.get('entities', {}).get('hashtags', [])

        # Check if any of the specified hashtags are present in the tweet
        if any(hashtag.lower() in [tag.get('text', '').lower() if isinstance(tag, dict) else str(tag).lower() for tag in tweet_hashtags] for hashtag in hashtags):
            filtered_data.append(tweet)

    return filtered_data

# Streamlit app
def main():
    st.title('Twitter Data Analysis')

    # Menu
    st.sidebar.title('Menu')
    choice = st.sidebar.selectbox('Choose Analysis Type', ['Full Analysis', 'Analysis by Hashtag'])

    # Process data based on user choice
    if choice == 'Full Analysis':
        data = demo_data
    elif choice == 'Analysis by Hashtag':
        user_hashtags = st.sidebar.text_input("Enter hashtags separated by commas (Example: tata, tatamotors)").split(',')
        user_hashtags = [hashtag.strip() for hashtag in user_hashtags]
        data = filter_data_by_hashtags(demo_data, user_hashtags)

    # Display sentiment and create graph
    if data:
        st.subheader('Sentiment Analysis')
        sentiment_scores = [analyze_sentiment(translate_text(tweet['text'])) for tweet in data]
        st.write(pd.Series(sentiment_scores).value_counts())

        st.subheader('Sentiment Graph')
        df = pd.DataFrame({'Sentiment': sentiment_scores})
        st.bar_chart(df['Sentiment'].value_counts())

if __name__ == "__main__":
    main()
