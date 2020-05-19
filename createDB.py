from models.vegetablesFruits import Vegetablesfruits
from models.animal import Animals
from models.food import Food
from models.action import Actions
import mlab
mlab.connect()


list_animals= [ 
        { 
            "image" : "../static/images/animal1.jpg",
            "word" : "Zebra",
            "pronunciation": "/ˈziːbrə/",
            "mean" : "Ngựa vằn",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/z/zeb/zebra/zebra__us_2.mp3",
        },
         { 
            "image" : "../static/images/animal2.jpg",
            "word" : "Giraffe",
            "pronunciation": "/dʒəˈræf/",
            "mean" : "Hươu cao cổ",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/g/gir/giraf/giraffe__us_1.mp3",
        },
        { 
            "image" : "../static/images/animal3.jpg",
            "word" : "Rhinoceros ",
            "pronunciation": "/raɪˈnɑːsərəs/",
            "mean" : "Tê giác",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/r/rhi/rhino/rhinoceros__us_1.mp3",
        },
          { 
            "image" : "../static/images/animal4.jpg",
            "word" : "Elephant",
            "pronunciation": "/ˈelɪfənt/",
            "mean" : "Con Voi",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/e/ele/eleph/elephant__us_1.mp3",
        },
        { 
            "image" : "../static/images/animal5.jpg",
            "word" : "Lion",
            "pronunciation": "/ˈlaɪən/",
            "mean" : "Sư tử",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/l/lio/lion_/lion__us_2.mp3",
        },
        { 
            "image" : "../static/images/animal6.jpg",
            "word" : "Tiger",
            "pronunciation": "/ˈtaɪɡər/",
            "mean" : "Con hổ",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/t/tig/tiger/tiger__us_1.mp3",
        },
         { 
            "image" : "../static/images/animal7.jpg",
            "word" : "Leopard",
            "pronunciation": "/ˈlepərd/",
            "mean" : "Con báo",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/l/leo/leopa/leopard__us_1.mp3",
        },
          { 
            "image" : "../static/images/animal8.jpg",
            "word" : "Hippopotamus",
            "pronunciation": "/ˌhɪpəˈpɑːtəməs/",
            "mean" : "Hà mã",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/h/hip/hippo/hippopotamus__us_1.mp3",
        },
         { 
            "image" : "../static/images/animal9.jpg",
            "word" : "Gnu",
            "pronunciation": "/nuː/",
            "mean" : "Linh dương đầu bò",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/g/gnu/gnu__/gnu__us_1.mp3",
        },
          { 
            "image" : "../static/images/animal10.jpg",
            "word" : "Antelope",
            "pronunciation": "/ˈæntɪləʊp/",
            "mean" : "Linh dương",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/a/ant/antel/antelope__us_1.mp3",
        },
         { 
            "image" : "../static/images/animal11.jpg",
            "word" : "Camel",
            "pronunciation": "/ˈkæml/",
            "mean" : "Lạc đà",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/c/cam/camel/camel__us_1.mp3",
        },
         { 
            "image" : "../static/images/animal12.jpg",
            "word" : "Eagle",
            "pronunciation": "/ˈiːɡl/",
            "mean" : "Đại bàng",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/e/eag/eagle/eagle__us_1.mp3",
        },
         { 
            "image" : "../static/images/animal13.jpg",
            "word" : "Owl",
            "pronunciation": "/aʊl/",
            "mean" : "Cú mèo",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/o/owl/owl__/owl__us_1.mp3",
        },
         { 
            "image" : "../static/images/animal14.jpg",
            "word" : "Falcon",
            "pronunciation": "/ˈfælkən/",
            "mean" : "Chim ưng",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/f/fal/falco/falcon__us_1_rr.mp3",
        },
         { 
            "image" : "../static/images/animal15.jpg",
            "word" : "Ostrich",
            "pronunciation": "/ˈɑːstrɪtʃ/",
            "mean" : "Đà điểu",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/o/ost/ostri/ostrich__us_1.mp3",
        },
         { 
            "image" : "../static/images/animal16.jpg",
            "word" : "Woodpecker",
            "pronunciation": "/ˈwʊdpekər/",
            "mean" : "Chim gõ kiến",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/w/woo/woodp/woodpecker__us_1.mp3",
        },
        
          ]
for i in list_animals:
    db = Animals( 
        image = i["image"],
        word = i["word"],
        pronunciation= i["pronunciation"],
        mean = i["mean"],
        audio_link = i["audio_link"]
                       
    )
#     db.save()

list_food = [
         { 
            "image" : "../static/images/food1.jpg",
            "word" : "Bacon",
            "pronunciation": "/ˈbeɪkən/",
            "mean" : "Thịt lợn muối xông khói",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/b/bac/bacon/bacon__us_1.mp3",
        },
         { 
            "image" : "../static/images/food2.jpg",
            "word" : "Sausage",
            "pronunciation": "/ˈsɔːsɪdʒ/",
            "mean" : "Xúc xích",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/s/sau/sausa/sausage__us_1_rr.mp3",
        },
         { 
            "image" : "../static/images/food3.jpg",
            "word" : "Ham",
            "pronunciation": "/hæm/",
            "mean" : "Thịt giăm bông",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/h/ham/ham__/ham__us_1.mp3",
        },
         { 
            "image" : "../static/images/food4.jpg",
            "word" : "Ice-cream",
            "pronunciation": "/ˈaɪs kriːm/",
            "mean" : "Kem",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/i/ice/ice_c/ice_cream_1_us_2.mp3",
        },
         { 
            "image" : "../static/images/food5.jpg",
            "word" : "Bread",
            "pronunciation": "/bred/",
            "mean" : "Bánh mỳ",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/b/bre/bread/bread__us_1.mp3",
        },
         { 
            "image" : "../static/images/food6.jpg",
            "word" : "Cheese",
            "pronunciation": "/tʃiːz/",
            "mean" : "Pho mát",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/c/che/chees/cheese__us_1.mp3",
        },
         { 
            "image" : "../static/images/food7.jpg",
            "word" : "Butter",
            "pronunciation": "/ˈbʌtər/",
            "mean" : "Bơ",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/b/but/butte/butter__us_2.mp3",
        },
         { 
            "image" : "../static/images/food8.jpg",
            "word" : "Cereal",
            "pronunciation": "/ˈsɪriəl/",
            "mean" : "Ngũ cốc",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/c/cer/cerea/cereal__us_1.mp3",
        },
         { 
            "image" : "../static/images/food9.jpg",
            "word" : "Steak",
            "pronunciation": "/steɪk/",
            "mean" : "Bò bít tết",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/s/ste/steak/steak__us_1.mp3",
        },
         { 
            "image" : "../static/images/food10.jpg",
            "word" : "Yogurt",
            "pronunciation": "/ˈjəʊɡərt/",
            "mean" : "Sữa chua",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/y/yog/yogur/yogurt__us_1.mp3",
        },
         { 
            "image" : "../static/images/food11.jpg",
            "word" : "Popcorn",
            "pronunciation": "/ˈpɑːpkɔːrn/",
            "mean" : "Bỏng ngô",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/p/pop/popco/popcorn__us_1.mp3",
        },
         { 
            "image" : "../static/images/food12.jpg",
            "word" : "Pasta",
            "pronunciation": "/ˈpɑːstə/",
            "mean" : "Mỳ ống",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/p/pas/pasta/pasta__us_1.mp3",
        },
         { 
            "image" : "../static/images/food13.jpg",
            "word" : "Biscuit",
            "pronunciation": "/ˈbɪskɪt/",
            "mean" : "Bánh quy",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/b/bis/biscu/biscuit__us_1.mp3",
        },
         { 
            "image" : "../static/images/food14.jpg",
            "word" : "Muffin",
            "pronunciation": "/ˈmʌfɪn/",
            "mean" : "Bánh nướng xốp",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/m/muf/muffi/muffin__us_1.mp3",
        },
         { 
            "image" : "../static/images/food15.jpg",
            "word" : "Pizza",
            "pronunciation": "/ˈpiːtsə/",
            "mean" : "Bánh pizza",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/p/piz/pizza/pizza__us_1.mp3",
        },
        { 
            "image" : "../static/images/food16.jpg",
            "word" : "Sandwich",
            "pronunciation": "/ˈsænwɪdʒ/",
            "mean" : "Bánh kẹp",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/s/san/sandw/sandwich__us_2.mp3",
        },
]
for i in list_food:
    db = Food( 
        image = i["image"],
        word = i["word"],
        pronunciation= i["pronunciation"],
        mean = i["mean"],
        audio_link = i["audio_link"]
                       
    )
#     db.save()
list_actions = [
    { 
            "image" : "../static/images/act1.jpg",
            "word" : "Adjust",
            "pronunciation": "/əˈdʒʌst/",
            "mean" : "Điều chỉnh",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/a/adj/adjus/adjust__us_1.mp3",
            "example" : "It's difficult to adjust to the new climate.",
    },
     { 
            "image" : "../static/images/act2.jpg",
            "word" : "Chase",
            "pronunciation": "/tʃeɪs/",
            "mean" : "Đuổi theo",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/c/cha/chase/chase__us_1.mp3",
            "example" : "You should chase your dreams.",
    },
     { 
            "image" : "../static/images/act3.jpg",
            "word" : "Control",
            "pronunciation": "/kənˈtrəʊl/",
            "mean" : "Điều khiển",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/x/xco/xcont/xcontrol__us_3.mp3",
            "example" : "My new car is quite easy to control.",
    },
     { 
            "image" : "../static/images/act4.jpg",
            "word" : "Convert",
            "pronunciation": "/kənˈvɜːrt/",
            "mean" : "Biến đổi",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/x/xco/xconv/xconvert__us_1.mp3",
            "example" : "You need to ensure that you've converted the data properly.",
    },
     { 
            "image" : "../static/images/act5.jpg",
            "word" : "Damage",
            "pronunciation": "/ˈdæmɪdʒ/",
            "mean" : "Làm hư hại",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/d/dam/damag/damage__us_1.mp3",
            "example" : "Don't damage my car !",
    },
     { 
            "image" : "../static/images/act6.jpg",
            "word" : "Decide",
            "pronunciation": "/dɪˈsaɪd/",
            "mean" : "Quyết định",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/d/dec/decid/decide__us_2.mp3",
            "example" : "Children will decide the future of Earth",
    },
     { 
            "image" : "../static/images/act7.jpg",
            "word" : "Defeat",
            "pronunciation": "/dɪˈfiːt/",
            "mean" : "Đánh bại",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/d/def/defea/defeat__us_1.mp3",
            "example" : "The goal is to defeat the enemy by whatever means possible.",
    },
     { 
            "image" : "../static/images/act8.webp",
            "word" : "Defend",
            "pronunciation": "/dɪˈfend/",
            "mean" : "Bảo vệ",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/d/def/defen/defend__us_4.mp3",
            "example" : "Why don't you defend yourself ?",
    },
     { 
            "image" : "../static/images/act9.png",
            "word" : "Reserve",
            "pronunciation": "/rɪˈzɜːrv/",
            "mean" : "Đặt trước",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/r/res/reser/reserve__us_4.mp3",
            "example" : "I just reserved my tickets.",
    },
     { 
            "image" : "../static/images/act10.jpg",
            "word" : "Rob",
            "pronunciation": "/rɑːb/",
            "mean" : "Cướp",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/r/rob/rob__/rob__us_1.mp3",
            "example" : "The tourists were robbed of their bags.",
    },
     { 
            "image" : "../static/images/act11.png",
            "word" : "Solve",
            "pronunciation": "/sɑːlv/",
            "mean" : "Giải quyết",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/s/sol/solve/solve__us_1_rr.mp3",
            "example" : "You can't solve anything by just running away.",
    },
     { 
            "image" : "../static/images/act12.webp",
            "word" : "Inspire",
            "pronunciation": "/ɪnˈspaɪər/",
            "mean" : "Truyền cảm hứng",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/i/ins/inspi/inspire__us_4.mp3",
            "example" : "The director inspired everybody on the project.",
    },
     { 
            "image" : "../static/images/act13.jpg",
            "word" : "Spoil",
            "pronunciation": "/spɔɪl/",
            "mean" : "Làm hỏng",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/s/spo/spoil/spoil__us_1.mp3",
            "example" : "Don't let him spoil your evening.",
    },
     { 
            "image" : "../static/images/act14.jpg",
            "word" : "Postpone",
            "pronunciation": "/pəʊˈspəʊn/",
            "mean" : "Trì hoãn",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/p/pos/postp/postpone__us_1.mp3",
            "example" : "They decided to postpone their holiday until next year.",
    },
     { 
            "image" : "../static/images/act15.jpg",
            "word" : "Offer",
            "pronunciation": "/ˈɔːfər/",
            "mean" : "Đề nghị",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/o/off/offer/offer__us_1_rr.mp3",
            "example" : "He offered $4000 for the car.",
    },
     { 
            "image" : "../static/images/act16.png",
            "word" : "Manage",
            "pronunciation": "/ˈmænɪdʒ/",
            "mean" : "Xoay sở",
            "audio_link": "https://www.oxfordlearnersdictionaries.com/media/english/us_pron/m/man/manag/manage__us_2.mp3",
            "example" : "How do you manage to get here ?",
    },

    
]
for i in list_actions:
    db = Actions( 
        image = i["image"],
        word = i["word"],
        pronunciation= i["pronunciation"],
        mean = i["mean"],
        audio_link = i["audio_link"],
        example= i["example"]
                       
    )
    # db.save()

