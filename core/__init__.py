from server.app import db
from server.models import Location


def populate_database():
    db.create_all()
    db.session.add(
        Location(
            id=1,
            name="Good Shepherd Ministries",
            description="Good Shepherd Ministries offer food, shelter, clothing and more to anyone in need. Monetary donations make a big difference in keeping the programs running and the lights and heat on for the long Toronto winter.: 412 Queen St E, Toronto, ON M5A 1T3",
            long=-79.362722,
            lat=43.656446,
            category="Soup Kitchens and Food Banks",
        )
    )
    db.session.add(
        Location(
            id=2,
            name="North York Harvest Food Bank",
            description="This food bank usually hosts a winter food drive that accepts nutritious, non-perishable food items that can be dropped off at local fire halls and participating supermarkets in the former borough of North York. It’s always in need of volunteers, if that’s something you’re interested in.: 116 Industry St, York, ON M6M 4L8",
            long=-79.493091,
            lat=43.69414,
            category="Soup Kitchens and Food Banks",
        )
    )
    db.session.add(
        Location(
            id=3,
            name="The Salvation Army",
            description="This organization’s Christmas Kettles campaign is one of its most visible projects (aiming to raise $21 million), but it uses the proceeds to provide essential services throughout the year in the form of food banks and community meals that feed over a million people annually : 107 Cedarvale Ave, East York, ON M4C 4J9",
            long=-79.311156,
            lat=43.687179,
            category="Soup Kitchens and Food Banks",
        )
    )
    db.session.add(
        Location(
            id=4,
            name="The Stop Community Food Centre",
            description="The Stop Community Food Centre offers a full spectrum of programs and services designed to increase food access and education, as well as a sense of community and civic engagement, including everything from cooking classes to community advocacy.: 1884 Davenport Rd, Toronto, ON M6N 4Y4",
            long=-79.45394,
            lat=43.670878,
            category="Soup Kitchens and Food Banks",
        )
    )
    db.session.add(
        Location(
            id=5,
            name="The Yonge Street Mission",
            description="The Yonge Street Mission has several different facilities to help those in need, from financially strapped families to newly arrived immigrants, seniors, socially marginalized adults, and homeless youth. No one is ever turned away. Food services is key component of outreach here.: 306 Gerrard St E, Toronto, ON M5A 2G7",
            long=-79.366474,
            lat=43.662474,
            category="Soup Kitchens and Food Banks",
        )
    )
    db.session.add(
        Location(
            id=6,
            name="Fort York Food Bank",
            description="The Fort York Food Bank has lots of volunteer opportunities on offer, from advocacy and counselling to graphic design and advertising. People can also aid with food sorting and community kitchen shifts, all in an effort to give everyone the chance to learn and grow.:380 College St, Toronto, ON M5T",
            long=-79.405135,
            lat=43.657304,
            category="Soup Kitchens and Food Banks",
        )
    )
    db.session.add(
        Location(
            id=7,
            name="Second Harvest",
            description="This not-for-profit has various initiatives and projects on the go all year round with proceeds directed toward feeding hungry children and families. Excess fresh food is delivered daily to hundreds of social service programs around the city.: 1450 Lodestar Rd, North York, ON M3J 3C1",
            long=--79.46869,
            lat=43.761126,
            category="Soup Kitchens and Food Banks",
        )
    )
    db.session.add(
        Location(
            id=8,
            name="Daily Bread Food Bank",
            description="The Daily Bread Food Bank is where many urgently needed food items can be found: baby food and formula, canned fish and meat, peanut butter, as well as canned fruits and vegetables. It will even help to arrange a pick-up if you have a contribution for their donation drives.: 191 New Toronto St, Etobicoke, ON M8V 2E7",
            long=-79.504103,
            lat=43.60645,
            category="Soup Kitchens and Food Banks",
        )
    )
    db.session.add(
        Location(
            id=9,
            name="Toronto Public Health",
            description="Certified facility for safe injections(SIS).: 277 Victoria Street, Toronto, ON M5B 1W2",
            long=-79.379342,
            lat=43.656568,
            category="Safe Injection Facilities",
        )
    )
    db.session.add(
        Location(
            id=10,
            name="South Riverdale Community Health Centre",
            description="Certified facility for safe injections (SIS): 955 Queen St E, Toronto, ON M4M 3P3",
            long=-79.33921,
            lat=43.661075,
            category="Safe Injection Facilities",
        )
    )
    db.session.add(
        Location(
            id=11,
            name="Fred Victor",
            description="Certified facility for safe injections(SIS).: 145 Queen St E, Toronto, ON M5C 1S1",
            long=-79.372972,
            lat=43.653626,
            category="Safe Injection Facilities",
        )
    )
    db.session.add(
        Location(
            id=12,
            name="Parkdale Queen West Community Health Centre",
            description="Certified facility for safe injections(SIS).: 168 Bathurst St, Toronto, ON M5V 2R4",
            long=-79.40422,
            lat=43.646621,
            category="Safe Injection Facilities",
        )
    )
    db.session.add(
        Location(
            id=13,
            name="Covenant House",
            description="Mission is to serve the suffering children and youth on the street and to protect and safeguard all children and youth with absolute respect and unconditional love.: 20 Gerrard St E, Toronto, ON M5B 2P3",
            long=-79.381435,
            lat=43.659504,
            category="Homeless Shelters",
        )
    )
    db.session.add(
        Location(
            id=14,
            name="Fred Victor",
            description="Fred Victor is a social service charitable organization that fosters long-lasting and positive change in the lives of homeless and low-income people living across Toronto.: 86 Lombard St Toronto ON M5C 1M3",
            long=-79.373961,
            lat=43.652307,
            category="Homeless Shelters",
        )
    )
    db.session.add(
        Location(
            id=15,
            name="Salvation Army The Gateway",
            description="Includes an emergency shelter for men and a drop-in centre for health-related issues :107 Jarvis St, Toronto, ON M5C 2H4",
            long=-79.372488,
            lat=43.652351,
            category="Homeless Shelters",
        )
    )
    db.session.add(
        Location(
            id=16,
            name="Maxwell Meighen Centre",
            description="The Maxwell Meighen Centre is a multi-care facility offering various programs and services. It is run on Christian principles and has a desire to share the love of God in a practical way with those experiencing homelessness in downtown Toronto.:135 Sherbourne St Toronto ON M5A 2R5",
            long=-79.369129,
            lat=43.655243,
            category="Homeless Shelters",
        )
    )
    db.session.add(
        Location(
            id=17,
            name="Arrabon House",
            description="Long term residential treatment program in group home environment with counselling services, community health, education, employment, life skills training and recreation programs.: 29 Wilson Park Rd Toronto, ON M6K 3B6",
            long=-79.441529,
            lat=43.63778,
            category="Residential Treatment Program",
        )
    )
    db.session.add(
        Location(
            id=18,
            name="Mary’ s Home",
            description="Mary’s Home can accommodate 38 women, aged 16 years or older, and we welcome women of different ages, cultures, religions.: Society of St Vincent de Paul 70 Gerrard St E Toronto ON M5B 1G6",
            long=-79.328437,
            lat=43.671203,
            category="Women Shelters",
        )
    )
    db.session.add(
        Location(
            id=19,
            name="Street Haven at the Crossroads",
            description="Street Haven at the Crossroads offers pathways for women experiencing or at risk of homelessness, through a variety of integrated services.: 87 Pembroke St Toronto ON M5A 2N9",
            long=-79.37243,
            lat=43.659243,
            category="Women Shelters",
        )
    )
    db.session.add(
        Location(
            id=20,
            name="Fred Victor Women’s Hostel",
            description="Women who turn to Fred Victor Women’s Hostel for shelter and support are welcomed into a safe environment. Our 44-bed emergency, overnight shelter is a safe-haven.:86 Lombard St Toronto ON M5C 1M3",
            long=-79.373961,
            lat=43.652307,
            category="Women Shelters",
        )
    )
    db.session.add(
        Location(
            id=21,
            name="Native Child and Family Services of Toronto",
            description="Child protection services. Family violence treatment and prevention including child sexual abuse,  individual and family counselling and  programs for women in abusive relationships.: 30 College St Toronto, ON M5G 1K2",
            long=-79.384558,
            lat=43.661342,
            category="Youth Shelters",
        )
    )
    db.session.add(
        Location(
            id=22,
            name="Turning Point Youth Services",
            description="Leaders in mental health, empowering youth to make positive change: 95 Wellesley St E Toronto ON M4Y 2X9",
            long=-79.379215,
            lat=43.665864,
            category="Mental Health Institutions",
        )
    )
    db.session.add(
        Location(
            id=23,
            name="The Salvation Army Harbour Light",
            description="Residential and community treatment programs :160 Jarvis St, Toronto, ON M5B 2E1",
            long=-79.37418,
            lat=43.655062,
            category="Mental Health Institutions",
        )
    )
    db.session.commit()
