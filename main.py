import tkinter as tk
from tkinter import messagebox, ttk


# ============================================================
# AI PLANT CARE ADVISOR - ADVANCED RULE-BASED EXPERT SYSTEM
# ============================================================


# ------------------------------------------------------------
# QUESTION DATA BANK (WITH DYNAMIC DEPENDENCY RULES)
# ------------------------------------------------------------

QUESTIONS = [
    {
        "id": 0,
        "question": "What type of plant are you caring for?",
        "options": [
            "Indoor plant",
            "Outdoor plant",
            "Flowering plant",
            "Vegetable / Herb",
            "Succulent / Cactus"
        ]
    },
    {
        "id": 1,
        "question": "Where is the plant currently placed?",
        "options": [
            "Bedroom",
            "Living room",
            "Balcony",
            "Garden",
            "Office"
        ]
    },
    {
        "id": 2,
        "question": "How old is the plant?",
        "options": [
            "Less than 3 months",
            "3 - 12 months",
            "1 - 3 years",
            "More than 3 years"
        ]
    },
    {
        "id": 3,
        "question": "How much sunlight does the plant receive daily?",
        "options": [
            "Less than 2 hours",
            "2 - 4 hours",
            "4 - 6 hours",
            "More than 6 hours"
        ]
    },
    {
        "id": 4,
        "question": "Is the sunlight direct or indirect?",
        "options": [
            "Direct sunlight",
            "Indirect sunlight",
            "Mostly shade"
        ]
    },
    {
        "id": 5,
        "question": "Does the plant receive morning sunlight?",
        "options": [
            "Yes",
            "No",
            "Sometimes"
        ]
    },
    {
        "id": 6,
        "question": "Does the plant receive strong afternoon sunlight?",
        "options": [
            "Yes",
            "No",
            "Sometimes"
        ]
    },
    {
        "id": 7,
        "question": "Do the leaves look faded or bleached?",
        "options": [
            "Yes",
            "No"
        ]
    },
    {
        "id": 8,
        "question": "How often do you water the plant?",
        "options": [
            "Every day",
            "Every 2 - 3 days",
            "Once a week",
            "Every 2 weeks",
            "Only when soil is dry"
        ]
    },
    {
        "id": 9,
        "question": "How much water do you normally give?",
        "options": [
            "Very little",
            "Moderate amount",
            "A lot of water"
        ]
    },
    {
        "id": 10,
        "question": "What is the current condition of the soil?",
        "options": [
            "Very dry",
            "Slightly dry",
            "Moist",
            "Very wet"
        ]
    },
    {
        "id": 11,
        "question": "Does water drain from the bottom of the pot?",
        "options": [
            "Yes",
            "No",
            "I don't know"
        ]
    },
    {
        "id": 12,
        "question": "Does the pot have drainage holes?",
        "options": [
            "Yes",
            "No",
            "I don't know"
        ]
    },
    {
        "id": 13,
        "question": "Does the soil remain wet for several days?",
        "options": [
            "Yes",
            "No",
            "Sometimes"
        ]
    },
    {
        "id": 14,
        "question": "What type of soil are you using?",
        "options": [
            "Potting soil",
            "Garden soil",
            "Sandy soil",
            "Clay / Heavy soil",
            "I don't know"
        ]
    },
    {
        "id": 15,
        "question": "Is the soil compact or hard?",
        "options": [
            "Yes",
            "No",
            "Sometimes"
        ]
    },
    {
        "id": 16,
        "question": "Does the soil drain quickly?",
        "options": [
            "Yes",
            "No",
            "I don't know"
        ]
    },
    {
        "id": 17,
        "question": "What type of pot are you using?",
        "options": [
            "Plastic",
            "Terracotta",
            "Ceramic",
            "Metal",
            "Other"
        ]
    },
    {
        "id": 18,
        "question": "Are the roots overcrowded or coming out of the pot?",
        "options": [
            "Yes",
            "No",
            "I don't know"
        ]
    },
    {
        "id": 19,
        "question": "Are the leaves turning yellow?",
        "options": [
            "Yes",
            "No",
            "A few leaves"
        ]
    },
    {
        "id": 20,
        "question": "Are the leaves turning brown?",
        "options": [
            "Yes",
            "No",
            "A few leaves"
        ]
    },
    {
        "id": 21,
        "question": "Are the leaf edges brown or crispy?",
        "options": [
            "Yes",
            "No"
        ]
    },
    {
        "id": 22,
        "question": "Are the leaves drooping?",
        "options": [
            "Yes",
            "No",
            "Sometimes"
        ]
    },
    {
        "id": 23,
        "question": "Are the leaves curling?",
        "options": [
            "Yes",
            "No",
            "Sometimes"
        ]
    },
    {
        "id": 24,
        "question": "Are leaves falling from the plant?",
        "options": [
            "Yes",
            "No",
            "A few leaves"
        ]
    },
    {
        "id": 25,
        "question": "Are there holes in the leaves?",
        "options": [
            "Yes",
            "No"
        ]
    },
    {
        "id": 26,
        "question": "Are there unusual spots on the leaves?",
        "options": [
            "Yes",
            "No"
        ]
    },
    {
        "id": 27,
        "question": "Can you see insects on the plant?",
        "options": [
            "Yes",
            "No",
            "Not sure"
        ]
    },
    {
        "id": 28,
        "question": "Are there tiny white insects?",
        "options": [
            "Yes",
            "No",
            "Not sure"
        ],
        "depends_on": 27,
        "required_answers": ["Yes", "Not sure"]
    },
    {
        "id": 29,
        "question": "Are there small black or green insects?",
        "options": [
            "Yes",
            "No",
            "Not sure"
        ],
        "depends_on": 27,
        "required_answers": ["Yes", "Not sure"]
    },
    {
        "id": 30,
        "question": "Is there a sticky substance on the leaves?",
        "options": [
            "Yes",
            "No",
            "Not sure"
        ],
        "depends_on": 27,
        "required_answers": ["Yes", "Not sure"]
    },
    {
        "id": 31,
        "question": "Is there web-like material around the leaves?",
        "options": [
            "Yes",
            "No",
            "Not sure"
        ],
        "depends_on": 27,
        "required_answers": ["Yes", "Not sure"]
    },
    {
        "id": 32,
        "question": "Is the plant growing normally?",
        "options": [
            "Yes",
            "No",
            "Very slowly"
        ]
    },
    {
        "id": 33,
        "question": "When was the plant last fertilized?",
        "options": [
            "Less than 1 month ago",
            "1 - 3 months ago",
            "More than 3 months ago",
            "Never",
            "I don't know"
        ]
    },
    {
        "id": 34,
        "question": "What is the main problem you are experiencing?",
        "options": [
            "Yellow leaves",
            "Brown leaves",
            "Drooping",
            "Slow growth",
            "Pests",
            "Root / Soil problem",
            "General plant care"
        ]
    }
]


# ------------------------------------------------------------
# EXPERT DIAGNOSTIC ENGINE & REASONING PIPELINE
# ------------------------------------------------------------

def diagnose(answers):

    scores = {
        "Overwatering": 0,
        "Underwatering": 0,
        "Insufficient Light": 0,
        "Excessive Sunlight": 0,
        "Poor Drainage": 0,
        "Pest Infestation": 0,
        "Possible Fungal Problem": 0,
        "Nutrient Deficiency": 0,
        "Root Bound / Pot Problem": 0
    }

    reasons = {key: [] for key in scores}

    # Overwatering Rules
    if answers.get(8) == "Every day":
        scores["Overwatering"] += 25
        reasons["Overwatering"].append("Watering frequency is daily.")
    if answers.get(8) == "Every 2 - 3 days":
        scores["Overwatering"] += 10
        reasons["Overwatering"].append("Frequent watering schedule detected.")
    if answers.get(10) == "Very wet":
        scores["Overwatering"] += 25
        reasons["Overwatering"].append("Soil is currently saturated and very wet.")
    if answers.get(13) == "Yes":
        scores["Overwatering"] += 20
        reasons["Overwatering"].append("Soil remains wet for several consecutive days.")
    if answers.get(19) == "Yes":
        scores["Overwatering"] += 15
        reasons["Overwatering"].append("Chlorosis (yellowing leaves) observed due to high moisture.")
    if answers.get(22) == "Sometimes":
        scores["Overwatering"] += 5

    # Underwatering Rules
    if answers.get(8) == "Only when soil is dry":
        scores["Underwatering"] += 10
    if answers.get(10) == "Very dry":
        scores["Underwatering"] += 25
        reasons["Underwatering"].append("Soil moisture level is critically dry.")
    if answers.get(22) == "Yes":
        scores["Underwatering"] += 20
        reasons["Underwatering"].append("Plant foliage is visibly drooping/wilting.")
    if answers.get(23) == "Yes":
        scores["Underwatering"] += 20
        reasons["Underwatering"].append("Leaves are curling due to moisture loss.")
    if answers.get(24) == "Yes":
        scores["Underwatering"] += 10
        reasons["Underwatering"].append("Plant is shedding leaves under water stress.")
    if answers.get(21) == "Yes":
        scores["Underwatering"] += 10
        reasons["Underwatering"].append("Crispy brown margins indicate foliage dehydration.")

    # Insufficient Light Rules
    if answers.get(3) == "Less than 2 hours":
        scores["Insufficient Light"] += 30
        reasons["Insufficient Light"].append("Plant gets under 2 hours of sunlight per day.")
    if answers.get(3) == "2 - 4 hours":
        scores["Insufficient Light"] += 15
        reasons["Insufficient Light"].append("Low daily photosynthetic light availability.")
    if answers.get(4) == "Mostly shade":
        scores["Insufficient Light"] += 25
        reasons["Insufficient Light"].append("Placement location is heavily shaded.")
    if answers.get(32) == "No":
        scores["Insufficient Light"] += 10
        reasons["Insufficient Light"].append("Vegetative growth has halted entirely.")
    if answers.get(34) == "Slow growth":
        scores["Insufficient Light"] += 15

    # Excessive Sunlight Rules
    if answers.get(4) == "Direct sunlight":
        scores["Excessive Sunlight"] += 15
        reasons["Excessive Sunlight"].append("Direct unshaded sun exposure.")
    if answers.get(6) == "Yes":
        scores["Excessive Sunlight"] += 25
        reasons["Excessive Sunlight"].append("Exposed to intense peak afternoon radiation.")
    if answers.get(7) == "Yes":
        scores["Excessive Sunlight"] += 15
        reasons["Excessive Sunlight"].append("Leaves display bleached or sun-faded discoloration.")
    if answers.get(21) == "Yes":
        scores["Excessive Sunlight"] += 15
        reasons["Excessive Sunlight"].append("Crispy leaf edges due to thermal scorch.")

    # Poor Drainage Rules
    if answers.get(11) == "No":
        scores["Poor Drainage"] += 30
        reasons["Poor Drainage"].append("Water is unable to drain properly out of the container.")
    if answers.get(12) == "No":
        scores["Poor Drainage"] += 25
        reasons["Poor Drainage"].append("Pot lacks fundamental drainage holes.")
    if answers.get(13) == "Yes":
        scores["Poor Drainage"] += 20
        reasons["Poor Drainage"].append("Soil traps moisture for extended periods.")
    if answers.get(14) == "Clay / Heavy soil":
        scores["Poor Drainage"] += 20
        reasons["Poor Drainage"].append("Heavy clay substrate compacts easily and restricts flow.")

    # Pest Infestation Rules
    if answers.get(27) == "Yes":
        scores["Pest Infestation"] += 30
        reasons["Pest Infestation"].append("Active insect presence confirmed on plant.")
    if answers.get(28) == "Yes":
        scores["Pest Infestation"] += 25
        reasons["Pest Infestation"].append("Tiny white insects (e.g., mealybugs, whiteflies) detected.")
    if answers.get(29) == "Yes":
        scores["Pest Infestation"] += 25
        reasons["Pest Infestation"].append("Aphids or dark insects detected feeding on sap.")
    if answers.get(30) == "Yes":
        scores["Pest Infestation"] += 25
        reasons["Pest Infestation"].append("Sticky honeydew secretions found on foliage.")
    if answers.get(31) == "Yes":
        scores["Pest Infestation"] += 25
        reasons["Pest Infestation"].append("Fine silk-like webbing detected (spider mites).")

    # Fungal Problem Rules
    if answers.get(26) == "Yes":
        scores["Possible Fungal Problem"] += 30
        reasons["Possible Fungal Problem"].append("Atypical spots or lesions present on foliage.")
    if answers.get(19) == "Yes":
        scores["Possible Fungal Problem"] += 15
    if answers.get(10) == "Very wet":
        scores["Possible Fungal Problem"] += 15
        reasons["Possible Fungal Problem"].append("Excess dampness creates ideal conditions for spores.")

    # Nutrient Deficiency Rules
    if answers.get(19) == "Yes":
        scores["Nutrient Deficiency"] += 20
        reasons["Nutrient Deficiency"].append("Yellowing leaves signal chlorosis or deficient minerals.")
    if answers.get(32) == "Very slowly":
        scores["Nutrient Deficiency"] += 20
        reasons["Nutrient Deficiency"].append("Growth rate is sluggish and stunted.")
    if answers.get(33) in ["More than 3 months ago", "Never"]:
        scores["Nutrient Deficiency"] += 30
        reasons["Nutrient Deficiency"].append("Lack of regular fertilizer feeding schedule.")

    # Root Bound Rules
    if answers.get(18) == "Yes":
        scores["Root Bound / Pot Problem"] += 40
        reasons["Root Bound / Pot Problem"].append("Roots are visibly constricted or emerging from bottom holes.")
    if answers.get(32) == "Very slowly":
        scores["Root Bound / Pot Problem"] += 15

    # Primary Problem Weighting
    main_problem = answers.get(34)
    if main_problem:
        if main_problem == "Yellow leaves":
            scores["Overwatering"] += 10
            scores["Nutrient Deficiency"] += 10
        elif main_problem == "Brown leaves":
            scores["Underwatering"] += 10
            scores["Excessive Sunlight"] += 10
        elif main_problem == "Drooping":
            scores["Underwatering"] += 15
            scores["Overwatering"] += 10
        elif main_problem == "Slow growth":
            scores["Insufficient Light"] += 15
            scores["Nutrient Deficiency"] += 15
        elif main_problem == "Pests":
            scores["Pest Infestation"] += 25
        elif main_problem == "Root / Soil problem":
            scores["Poor Drainage"] += 20
            scores["Root Bound / Pot Problem"] += 20

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    diagnosis_name = sorted_scores[0][0]
    highest_score = sorted_scores[0][1]

    confidence = min(95, max(45, highest_score))
    selected_reasons = reasons[diagnosis_name]

    if not selected_reasons:
        selected_reasons.append("Environmental parameter combinations match known diagnostic patterns.")

    return diagnosis_name, confidence, sorted_scores, selected_reasons


# ------------------------------------------------------------
# RECOMMENDATION KNOWLEDGE DATABASE
# ------------------------------------------------------------

RECOMMENDATIONS = {
    "Overwatering": {
        "icon": "💧",
        "description": "The plant is receiving too much water, suffocating root oxygen intake.",
        "watering": "Allow top 2–3 cm of soil to dry completely before next watering cycle.",
        "light": "Provide healthy indirect sunlight to encourage natural evaporation.",
        "soil": "Use well-draining soil mixed with coarse sand or perlite.",
        "action": "Inspect roots for soft rot and carefully prune away damaged black roots."
    },
    "Underwatering": {
        "icon": "🥀",
        "description": "The plant is experiencing dehydration and moisture starvation.",
        "watering": "Water thoroughly until water drains smoothly out of bottom holes.",
        "light": "Protect plant temporarily from harsh direct sunlight.",
        "soil": "Ensure soil absorbs water evenly without letting water run down dry side gaps.",
        "action": "Prune crispy foliage and maintain a consistent soil-moisture check schedule."
    },
    "Insufficient Light": {
        "icon": "☀️",
        "description": "The plant lacks adequate light energy required for efficient photosynthesis.",
        "watering": "Reduce watering frequency as dark plants consume water slowly.",
        "light": "Move to a brighter location with optimal indirect sunlight.",
        "soil": "Ensure substrate is well-aerated.",
        "action": "Rotate the pot weekly to ensure balanced growth on all sides."
    },
    "Excessive Sunlight": {
        "icon": "🔥",
        "description": "Intense sunlight radiation is scorching delicate leaf surfaces.",
        "watering": "Water consistently to maintain steady subterranean moisture.",
        "light": "Move back from hot window glass or use a sheer curtain.",
        "soil": "Ensure soil retains adequate moisture without drying into rock-hard crust.",
        "action": "Trim severely sunburned foliage after the plant stabilizes."
    },
    "Poor Drainage": {
        "icon": "🪴",
        "description": "Water is getting trapped around root zones, cutting off root oxygen.",
        "watering": "Pause watering until excess standing water evaporates entirely.",
        "light": "Maintain solid ambient light and clear air movement around pot.",
        "soil": "Repot using porous soil containing perlite or pumice.",
        "action": "Ensure container drainage holes are unobstructed."
    },
    "Pest Infestation": {
        "icon": "🐛",
        "description": "Insects are sucking essential plant sap and damaging leaves.",
        "watering": "Water soil directly—keep foliage clean and dry.",
        "light": "Maintain standard required ambient lighting.",
        "soil": "Keep topsoil clear of dead fallen foliage.",
        "action": "Isolate plant immediately. Spray leaves thoroughly with neem oil or insecticidal soap."
    },
    "Possible Fungal Problem": {
        "icon": "🍃",
        "description": "High dampness or stagnant moisture has triggered fungal spot growth.",
        "watering": "Avoid splashing water on foliage when watering.",
        "light": "Position in a well-ventilated area with bright indirect light.",
        "soil": "Use fresh, clean, well-draining potting mixture.",
        "action": "Prune spotted leaves and dispose of them far from healthy plants."
    },
    "Nutrient Deficiency": {
        "icon": "🌿",
        "description": "Essential minerals (e.g., nitrogen, potassium) are depleted from soil.",
        "watering": "Water regularly to facilitate mineral absorption.",
        "light": "Provide optimal light to drive nutrient uptake.",
        "soil": "Top-dress with rich compost or fresh potting mix.",
        "action": "Apply a balanced liquid fertilizer diluted to half-strength."
    },
    "Root Bound / Pot Problem": {
        "icon": "🪴",
        "description": "Roots have completely filled the container, choking room for expansion.",
        "watering": "Check soil daily as root-heavy pots dry out very fast.",
        "light": "Maintain normal plant light conditions.",
        "soil": "Prepare a fresh batch of well-draining potting soil.",
        "action": "Repot into a container 2 to 3 inches wider in diameter."
    }
}


# ============================================================
# GUI APPLICATION (TKINTER)
# ============================================================

class PlantCareApp:

    def __init__(self, root):
        self.root = root
        self.root.title("AI Plant Care Advisor — Professional Expert System")
        self.root.geometry("980x720")
        self.root.minsize(880, 640)
        self.root.configure(bg="#F4F8F1")

        # System State Variables
        self.answers = {}
        self.active_questions = []
        self.current_index = 0

        self.setup_styles()
        self.show_home()

    def setup_styles(self):
        self.title_font = ("Segoe UI", 26, "bold")
        self.heading_font = ("Segoe UI", 20, "bold")
        self.question_font = ("Segoe UI", 20, "bold")
        self.normal_font = ("Segoe UI", 11)
        self.bold_font = ("Segoe UI", 11, "bold")
        self.option_font = ("Segoe UI", 12)
        self.small_font = ("Segoe UI", 10)

        self.green = "#2F6B3B"
        self.dark_green = "#214D2B"
        self.light_green = "#E7F2E4"
        self.bg = "#F4F8F1"

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def evaluate_active_questions(self):
        """Dynamic Expert System Logic: Filters out questions that are irrelevant based on past answers."""
        self.active_questions = []
        for q in QUESTIONS:
            if "depends_on" in q:
                parent_id = q["depends_on"]
                parent_ans = self.answers.get(parent_id)
                if parent_ans in q["required_answers"]:
                    self.active_questions.append(q)
            else:
                self.active_questions.append(q)

    # --------------------------------------------------------
    # HOME SCREEN
    # --------------------------------------------------------

    def show_home(self):
        self.clear_screen()

        container = tk.Frame(self.root, bg=self.bg)
        container.pack(fill="both", expand=True)

        tk.Label(container, text="🌿", font=("Segoe UI Emoji", 55), bg=self.bg).pack(pady=(40, 0))
        tk.Label(container, text="AI Plant Care Advisor", font=self.title_font, fg=self.dark_green, bg=self.bg).pack(pady=(5, 2))
        tk.Label(container, text="Rule-Based Expert System & Inference Engine", font=("Segoe UI", 13), fg="#55705A", bg=self.bg).pack()

        card = tk.Frame(container, bg="white", highlightthickness=1, highlightbackground="#D6E4D2")
        card.pack(padx=100, pady=25, fill="x")

        tk.Label(card, text="🌱 Expert Diagnostics", font=self.heading_font, fg=self.dark_green, bg="white").pack(pady=(20, 10))
        tk.Label(
            card,
            text=(
                "Answer key diagnostic questions regarding your plant's environment.\n"
                "Our rule-based engine dynamically evaluates parameters, filters questions,\n"
                "and delivers precise primary diagnoses with key reasons."
            ),
            font=self.normal_font,
            fg="#555555",
            bg="white",
            justify="center"
        ).pack(pady=5)

        tk.Label(card, text="✓ Dynamic Rules   ✓ Key Factor Analysis   ✓ Answer Adjustment", font=self.bold_font, fg=self.green, bg="white").pack(pady=15)

        start_btn = tk.Button(
            card,
            text="START DIAGNOSIS  →",
            command=self.start_diagnosis,
            font=("Segoe UI", 12, "bold"),
            bg=self.green,
            fg="white",
            activebackground=self.dark_green,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=12
        )
        start_btn.pack(pady=(10, 25))

        tk.Label(container, text="AI Expert System • Adaptive Inference • Plant Health Analytics", font=self.small_font, fg="#718071", bg=self.bg).pack(side="bottom", pady=15)

    def start_diagnosis(self):
        self.answers = {}
        self.current_index = 0
        self.evaluate_active_questions()
        self.show_question()

    # --------------------------------------------------------
    # HIGH-LEVEL PROFESSIONAL QUESTION SCREEN
    # --------------------------------------------------------

    def show_question(self):
        self.clear_screen()
        self.evaluate_active_questions()

        if self.current_index >= len(self.active_questions):
            self.show_result()
            return

        q = self.active_questions[self.current_index]

        # Header Bar
        header = tk.Frame(self.root, bg=self.dark_green, height=65)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(header, text="🌿 AI PLANT CARE ADVISOR", font=("Segoe UI", 15, "bold"), fg="white", bg=self.dark_green).pack(side="left", padx=25, pady=18)
        tk.Label(header, text=f"QUESTION {self.current_index + 1} / {len(self.active_questions)}", font=("Segoe UI", 10, "bold"), fg="#DCEBDD", bg=self.dark_green).pack(side="right", padx=25)

        main = tk.Frame(self.root, bg=self.bg)
        main.pack(fill="both", expand=True, padx=50, pady=15)

        # Progress Calculation
        progress_val = ((self.current_index + 1) / len(self.active_questions)) * 100

        progress_frame = tk.Frame(main, bg=self.bg)
        progress_frame.pack(fill="x", pady=(0, 10))

        progress_bg = tk.Frame(progress_frame, bg="#DCE8D9", height=6)
        progress_bg.pack(fill="x")

        progress_bar = tk.Frame(progress_bg, bg=self.green, height=6, width=int(800 * progress_val / 100))
        progress_bar.place(x=0, y=0)

        # Card Container
        card = tk.Frame(main, bg="white", highlightthickness=1, highlightbackground="#D6E4D2")
        card.pack(fill="both", expand=True)

        tk.Label(card, text=f"Step {self.current_index + 1}", font=("Segoe UI", 11, "bold"), fg=self.green, bg="white").pack(pady=(20, 2))
        tk.Label(card, text=q["question"], font=self.question_font, fg="#263A29", bg="white", wraplength=760, justify="center").pack(pady=(2, 20))

        # Selected Option Variable
        self.selected_option = tk.StringVar(value="")
        if q["id"] in self.answers:
            self.selected_option.set(self.answers[q["id"]])

        options_container = tk.Frame(card, bg="white")
        options_container.pack(fill="both", expand=True, padx=120)

        self.option_cards = []

        for option in q["options"]:
            # Card frame for option styling
            opt_card = tk.Frame(
                options_container,
                bg="white",
                highlightthickness=1,
                highlightbackground="#E0E8DF"
            )
            opt_card.pack(fill="x", pady=4, ipady=3)

            rb = tk.Radiobutton(
                opt_card,
                text=option,
                value=option,
                variable=self.selected_option,
                font=self.option_font,
                fg="#38483B",
                bg="white",
                activebackground="white",
                activeforeground=self.dark_green,
                selectcolor="white",
                anchor="w",
                padx=15,
                pady=6,
                cursor="hand2",
                tristatevalue="x",
                command=lambda opt=option: self.on_option_selected(opt)
            )
            rb.pack(fill="x", expand=True)

            # Bind frame click to radio selection
            opt_card.bind("<Button-1>", lambda e, opt=option: self.on_option_selected(opt))
            rb.bind("<Button-1>", lambda e, opt=option: self.on_option_selected(opt))

            self.option_cards.append((option, opt_card, rb))

        # Highlight if pre-selected
        if self.selected_option.get():
            self.update_option_styles(self.selected_option.get())

        # Navigation Controls
        navigation = tk.Frame(card, bg="white")
        navigation.pack(fill="x", padx=30, pady=20)

        prev_btn = tk.Button(
            navigation,
            text="← Previous",
            command=self.previous_question,
            font=("Segoe UI", 10, "bold"),
            bg="#E8EEE6",
            fg=self.dark_green,
            activebackground="#DCE8D9",
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=8
        )
        if self.current_index == 0:
            prev_btn.config(state="disabled")
        prev_btn.pack(side="left")

        btn_text = "ANALYZE PLANT  ✓" if self.current_index == len(self.active_questions) - 1 else "Next  →"

        next_btn = tk.Button(
            navigation,
            text=btn_text,
            command=self.next_question,
            font=("Segoe UI", 10, "bold"),
            bg=self.green,
            fg="white",
            activebackground=self.dark_green,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=22,
            pady=8
        )
        next_btn.pack(side="right")

    def on_option_selected(self, val):
        self.selected_option.set(val)
        self.update_option_styles(val)

    def update_option_styles(self, selected_val):
        """Highlights the selected option card with green border and soft background."""
        for option, card_frame, rb in self.option_cards:
            if option == selected_val:
                card_frame.config(bg="#EAF4E8", highlightbackground=self.green, highlightthickness=2)
                rb.config(bg="#EAF4E8", selectcolor="#EAF4E8", fg=self.dark_green, font=("Segoe UI", 12, "bold"))
            else:
                card_frame.config(bg="white", highlightbackground="#E0E8DF", highlightthickness=1)
                rb.config(bg="white", selectcolor="white", fg="#38483B", font=self.option_font)

    def next_question(self):
        ans = self.selected_option.get()
        if not ans:
            messagebox.showwarning("Answer Required", "Please select an answer before continuing.")
            return

        current_q_id = self.active_questions[self.current_index]["id"]
        self.answers[current_q_id] = ans

        if self.current_index < len(self.active_questions) - 1:
            self.current_index += 1
            self.show_question()
        else:
            self.show_result()

    def previous_question(self):
        if self.current_index > 0:
            if self.selected_option.get():
                current_q_id = self.active_questions[self.current_index]["id"]
                self.answers[current_q_id] = self.selected_option.get()
            self.current_index -= 1
            self.show_question()

    # --------------------------------------------------------
    # FINAL RESULT SCREEN + ADJUST ANSWERS MODAL
    # --------------------------------------------------------

    def show_result(self):
        diagnosis, confidence, all_scores, reasons = diagnose(self.answers)
        self.clear_screen()

        rec = RECOMMENDATIONS[diagnosis]

        header = tk.Frame(self.root, bg=self.dark_green, height=65)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(header, text="🌿 PLANT ANALYSIS RESULT", font=("Segoe UI", 16, "bold"), fg="white", bg=self.dark_green).pack(pady=18)

        # Scrollable Frame Area
        canvas = tk.Canvas(self.root, bg=self.bg, highlightthickness=0)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)

        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        content = tk.Frame(canvas, bg=self.bg)
        canvas_window = canvas.create_window((0, 0), window=content, anchor="nw")

        def configure_content(event):
            canvas.itemconfig(canvas_window, width=event.width)

        canvas.bind("<Configure>", configure_content)
        content.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Diagnosis Card
        diag_card = tk.Frame(content, bg="white", highlightthickness=1, highlightbackground="#D6E4D2")
        diag_card.pack(padx=60, pady=(20, 15), fill="x")

        tk.Label(diag_card, text=rec["icon"], font=("Segoe UI Emoji", 36), bg="white").pack(pady=(15, 0))
        tk.Label(diag_card, text="PRIMARY DIAGNOSIS", font=("Segoe UI", 9, "bold"), fg="#718071", bg="white").pack(pady=(2, 2))
        tk.Label(diag_card, text=diagnosis.upper(), font=("Segoe UI", 22, "bold"), fg=self.dark_green, bg="white").pack()
        tk.Label(diag_card, text=f"Confidence Level: {confidence}%", font=("Segoe UI", 11, "bold"), fg=self.green, bg="white").pack(pady=4)

        tk.Label(diag_card, text=rec["description"], font=self.normal_font, fg="#555555", bg="white", wraplength=680, justify="center").pack(pady=(2, 15))

        conf_bg = tk.Frame(diag_card, bg="#DCE8D9", height=8)
        conf_bg.pack(fill="x", padx=80, pady=(0, 20))

        conf_bar = tk.Frame(conf_bg, bg=self.green, height=8)
        conf_bar.place(x=0, y=0, relwidth=confidence / 100)

        # REASONS SECTION
        reason_card = tk.Frame(content, bg="#F9FBF8", highlightthickness=1, highlightbackground="#C8DBC3")
        reason_card.pack(padx=60, pady=8, fill="x")

        tk.Label(reason_card, text="🔍 DIAGNOSIS REASONS & KEY FACTORS", font=("Segoe UI", 11, "bold"), fg=self.dark_green, bg="#F9FBF8").pack(anchor="w", padx=20, pady=(12, 6))

        for r in reasons:
            r_frame = tk.Frame(reason_card, bg="#F9FBF8")
            r_frame.pack(anchor="w", padx=20, pady=2)
            tk.Label(r_frame, text="•", font=("Segoe UI", 12, "bold"), fg=self.green, bg="#F9FBF8").pack(side="left", padx=(0, 5))
            tk.Label(r_frame, text=r, font=self.normal_font, fg="#334235", bg="#F9FBF8", wraplength=620, justify="left").pack(side="left")

        tk.Frame(reason_card, bg="#F9FBF8", height=10).pack()

        # Action Recommendations
        self.create_recommendation_card(content, "💧  WATERING GUIDE", rec["watering"])
        self.create_recommendation_card(content, "☀️  SUNLIGHT REQUIREMENT", rec["light"])
        self.create_recommendation_card(content, "🪴  SOIL & POT MANAGEMENT", rec["soil"])
        self.create_recommendation_card(content, "🌿  RECOMMENDED ACTION STEP", rec["action"])

        # Other Possible Conditions
        other_card = tk.Frame(content, bg="white", highlightthickness=1, highlightbackground="#D6E4D2")
        other_card.pack(padx=60, pady=10, fill="x")

        tk.Label(other_card, text="📊 OTHER POSSIBLE CONDITIONS CONSIDERED", font=("Segoe UI", 11, "bold"), fg=self.dark_green, bg="white").pack(anchor="w", padx=20, pady=(15, 8))

        for name, score in all_scores[1:5]:
            if score > 0:
                row = tk.Frame(other_card, bg="white")
                row.pack(fill="x", padx=20, pady=3)
                tk.Label(row, text=name, font=self.normal_font, fg="#4A584C", bg="white").pack(side="left")
                tk.Label(row, text=f"{min(score, 95)}% match", font=("Segoe UI", 10, "bold"), fg=self.green, bg="white").pack(side="right")

        tk.Frame(other_card, bg="white", height=10).pack()

        # ACTION BUTTON BAR (OK, RESTART & ADJUST)
        button_frame = tk.Frame(content, bg=self.bg)
        button_frame.pack(pady=25)

        ok_btn = tk.Button(
            button_frame,
            text="✓  OK / DONE",
            command=self.show_home,
            font=("Segoe UI", 11, "bold"),
            bg="#3B7A48",
            fg="white",
            activebackground=self.dark_green,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10
        )
        ok_btn.pack(side="left", padx=8)

        adjust_btn = tk.Button(
            button_frame,
            text="⚙️  ADJUST ANSWERS",
            command=self.open_adjust_window,
            font=("Segoe UI", 11, "bold"),
            bg="#316B70",
            fg="white",
            activebackground="#1E474B",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10
        )
        adjust_btn.pack(side="left", padx=8)

        restart_btn = tk.Button(
            button_frame,
            text="↻  RESTART DIAGNOSIS",
            command=self.start_diagnosis,
            font=("Segoe UI", 11, "bold"),
            bg="#1E4D2B",
            fg="white",
            activebackground="#14361E",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10
        )
        restart_btn.pack(side="left", padx=8)

        tk.Label(
            content,
            text="Note: Expert inference output is generated based on strict rule-based evaluation.",
            font=self.small_font,
            fg="#777777",
            bg=self.bg,
            wraplength=650,
            justify="center"
        ).pack(pady=(0, 25))

    def create_recommendation_card(self, parent, title, text):
        card = tk.Frame(parent, bg="white", highlightthickness=1, highlightbackground="#D6E4D2")
        card.pack(padx=60, pady=5, fill="x")

        tk.Label(card, text=title, font=("Segoe UI", 11, "bold"), fg=self.dark_green, bg="white").pack(anchor="w", padx=20, pady=(12, 3))
        tk.Label(card, text=text, font=self.normal_font, fg="#444444", bg="white", wraplength=660, justify="left").pack(anchor="w", padx=20, pady=(0, 12))

    # --------------------------------------------------------
    # ADJUST / EDIT ANSWERS DIALOG WINDOW
    # --------------------------------------------------------

    def open_adjust_window(self):
        """Allows jumping to any answered question to edit parameters."""
        adjust_win = tk.Toplevel(self.root)
        adjust_win.title("Adjust Diagnostic Inputs")
        adjust_win.geometry("600x500")
        adjust_win.configure(bg="#F4F8F1")
        adjust_win.grab_set()

        tk.Label(adjust_win, text="⚙️ Adjust Answered Inputs", font=("Segoe UI", 14, "bold"), fg=self.dark_green, bg="#F4F8F1").pack(pady=15)
        tk.Label(adjust_win, text="Select a question below to modify your response:", font=self.small_font, fg="#555555", bg="#F4F8F1").pack()

        list_frame = tk.Frame(adjust_win, bg="white", highlightthickness=1, highlightbackground="#D6E4D2")
        list_frame.pack(fill="both", expand=True, padx=20, pady=15)

        lb_scroll = tk.Scrollbar(list_frame)
        lb_scroll.pack(side="right", fill="y")

        listbox = tk.Listbox(list_frame, font=self.normal_font, yscrollcommand=lb_scroll.set, relief="flat", highlightthickness=0)
        listbox.pack(fill="both", expand=True, padx=5, pady=5)
        lb_scroll.config(command=listbox.yview)

        # Populate listbox with answered questions
        answered_q_ids = list(self.answers.keys())
        for q_id in answered_q_ids:
            q_text = QUESTIONS[q_id]["question"]
            ans_text = self.answers[q_id]
            listbox.insert("end", f"• {q_text} → [{ans_text}]")

        def jump_to_selected():
            sel = listbox.curselection()
            if not sel:
                messagebox.showwarning("Selection Required", "Please choose an answer from the list.", parent=adjust_win)
                return
            
            selected_q_id = answered_q_ids[sel[0]]
            adjust_win.destroy()
            
            # Find index in active list
            self.evaluate_active_questions()
            for idx, q in enumerate(self.active_questions):
                if q["id"] == selected_q_id:
                    self.current_index = idx
                    break
            self.show_question()

        jump_btn = tk.Button(
            adjust_win,
            text="Edit Selected Question",
            command=jump_to_selected,
            font=("Segoe UI", 11, "bold"),
            bg=self.green,
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        )
        jump_btn.pack(pady=(0, 15))


# ============================================================
# MAIN ENTRY POINT
# ============================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = PlantCareApp(root)
    root.mainloop()
