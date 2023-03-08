''' views.py contains the funtions to render the webpages
    some functions will use the information in the lists and dictionaries here
    to render the information on the webpages.'''

# import libraries
from django.shortcuts import render

# lists and dictionaries used to populate the index and details webpages
skills = ['Python', 'HTML',
          'MySQL', 'MS Offcie',
          'Moodle', 'Mahara',
          'Kaltura', 'WordPress',
          'CSS']

languages = {'English': 'Native',
             'Turkish': 'Native',
             'Chinese': 'Intermediate (HSK4)'}

about_me = ["Physicist, scientist, project manager, teacher, educational"
            " technologist and now an aspiring software engineer.",
            "I have worn a number of hats already and I look forward to trying "
            "on a few more. In my time as a researcher, I have had the opportunity "
            "to contribute to the wider science community by inventing new apparatus "
            "and publications in journals. As a dynamic person I feel I brought much "
            "to the teaching profession. I have been working with young people for many "
            "years. I worked as a Teacher of Science and Mathematics in various educational "
            "settings. Technology has always interested me, and in schools I have always "
            "searched for ways on how to best use ICT as a teaching and learning resource; "
            "be it facilitating staff training or creating cross-curricular creative ICT "
            "based teaching projects.", "During my travels in China and South-east Asia, "
            "I became involved in some local projects such as setting up a local market-space "
            "website for locals to use to exchange second hand goods. This has inspired me to "
            "learn how to program which led me to take online courses by Harvard and Microsoft "
            "during my travels. This has lead me to combine my experience in education and "
            "technology to consult and work as an educational technologist in Russel Group "
            "universities in the UK; where I have lead many projects on creating learning "
            "and instructional design, and develop and enhance the use of virtual learning "
            "environments. Working on these projects, I have again realised that I really "
            "enjoyed the creative side of programming where I was able to bring ideas to "
            "life in the digital realm.", "Having had no real formal programming education "
            "has lead me to apply for a Software Engineering Bootcamp at HyperionDev sponsored "
            "by the DfE and lucky to be one of the lucky few to be accepted. At HyperionDev "
            "the access to mentors and lecturers to get feedback on your code and to be able "
            "to discuss and ask questions would greatly help to understand ones progress. "
            "By the end of the bootcamp I hope to be confident in my programming abilities "
            "to be able to pursue projects that I was not previously confident in taking on."
            ]

uni_edu = {"PGCE: Secondary Science with Physics Specialism":
           "Institute of Education (UCL)",
           "MRes in Protein Membrane Chemical Biology":
           "Imperial College London",
           "MSci Physics (4 years, 2:1)": "Imperial College London"}

specialist_courses = {"HyperionDev": "Software Engineering Bootcamp",
                      "Microsoft Professional Program Certificate in Artificial Intelligence":
                      "Capstone Project: Categorizing World Health Organisation Publications",
                      "Microsoft Professional Program Certificate in Data Science":
                      "Capstone Project: Predicting County Level Rents in the USA",
                      "HarvardX (Harvard University) CS50 Computer Science":
                      "Final Project: Photo organiser using image recognition",
                      "PI-Management": "Knowledge Transfer Partnership Management Course"}

projects = {"All my projects can be viewed on my GitHub page.":
            "https://github.com/hak1979?tab=repositories"}

publications = {"A micro-pressure system for measuring single cell adhesion: "
                "application to cancer cell lines of different metastatic potential "
                "and voltage-gated Na+ channel expression. (Eur Biophys J. 2007 Sep "
                "19; 17879092)": "https://www.researchgate.net/publication/"
                "5964189_Single_cell_adhesion_measuring_apparatus_SCAMA_Application"
                "_to_cancer_cell_lines_of_different_metastatic_potential_and_voltage"
                "-gated_Na_channel_expression",
                "Angiogenic Functions of Voltage-Gated Na+ Channels in Human "
                "Endothelial Cells Modulation of Vascular Endothelial Growth Factor "
                "(VEGF) Signalling. (The Journal of Biological Chemistry, Amer Soc "
                "Biochemistry Molecular Biology Inc, 2011: 21385874)":
                "https://pubmed.ncbi.nlm.nih.gov/21385874/",
                "The Importance of Chios Goats in Turkey. (Journal of Agricultural "
                "Science and Technology, Volume 4, Number 4A, April 2014; 21616256)": None}

employment = {
    "Freelance Educational Technologist":
    ["Providing IT solutions to clients for a variety of projects including:",
     ["Web-Design", "Bespoke applications", "Educational VLE design and implementation"]],
    "CARA NGO - Freelance Educational Technologist":
    ["Take an active role in the instructional design, development of online teaching "
     "in collaboration with colleagues",
     "Develop and enhance the use of a bespoke virtual learning environment",
     "Liaise with internal and external colleagues to ensure the work is successfully "
     "completed within tight deadlines",
     "Set up and configure functionality in relevant systems to facilitate the project’s progress",
     "Build new course areas, quizzes and assessment submission templates",
     "To provide technical support on asynchronous learning",
     "Edit media, embed recorded live sessions or other videos on the course site"],
    "Queen Mary University London – Learning Technologist":
    ["Lead on creating both the learning and instructional design for the identified "
     "online learning pre-sessional modules",
     "Lead the storylining, teaching, learning and assessment propose, and implement "
     "instructional design solutions",
     "Lead on training, promotion and communication activities to support the successful "
     "rollout and sustainable use "
     "of the outputs from this workstream",
     "Take an active role in the instructional design, development of online teaching in "
     "collaboration with colleagues",
     "Develop and enhance the use of QMplus; QMUL’s Moodle-based virtual learning environment",
     "Enhance the use of QMplus Hub; QMUL’s Mahara based eProtfolio system",
     "Liaising with internal and external colleagues to ensure the work is successfully completed "
     "within tight deadlines",
     "To complete the successful specification, design and implementation of new online teaching "
     "materials. In particular, to:",
     ["Co-ordinate and contribute to new development of materials in Moodle and other appropriate "
      "technologies",
      "Set up and configure functionality in relevant systems to facilitate the project’s progress",
      "Build materials in Moodle, such as new course areas, quizzes and assessment submission templates",
      "To provide technical support during online synchronous teaching and asynchronous learning"]],
    "Lived and travelled in Southeast Asia":
    ["Immersed myself in Southeast Asian culture and traditions. Took part in local projects to enhance the "
     "lives of the local people, taught English and organised events of cultural exchange. Also became "
     "involved in some projects such as setting up a local market-space website for locals to use to exchange "
     "second hand goods. This has inspired me to learn how to program which led me to take online courses by "
     "Harvard and Microsoft during my travels."]}

# Create your views here.


def index(request):
    '''Function to render the index page
        The function uses the information in the lists and dictionaries to display
        the informationon the page.'''
    return render(request, "index.html", {
        "skills": skills,
        "languages": languages,
        "about_me": about_me,
        "uni_edu": uni_edu,
        "specialist_courses": specialist_courses,
        "projects": projects,
        "publications": publications,
        "employment": employment
    })


def details(request):
    '''Function to render the details page
        The function uses the information in the lists and dictionaries to display
        the informationon the page.'''
    return render(request, "details.html", {
        "skills": skills,
        "languages": languages,
        "about_me": about_me,
        "uni_edu": uni_edu,
        "specialist_courses": specialist_courses,
        "projects": projects,
        "publications": publications,
        "employment": employment
    })


def shop(request):
    '''Function to render the shop page'''
    return render(request, "shop.html")
