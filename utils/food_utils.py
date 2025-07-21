# utils/food_utils.py

import plotly.graph_objects as go

# 🌱 Nutritional Advice for Each Marker
NUTRITION_MAP = {
    "hemoglobin": {
        "deficiency": "Low Hemoglobin (possible Iron Deficiency)",
        "recommend": ["Spinach", "Liver", "Beetroot", "Dates", "Pomegranate"],
        "nutrient": "Iron"
    },
    "iron": {
        "deficiency": "Low Iron Detected",
        "recommend": ["Spinach", "Liver", "Pumpkin seeds", "Tofu", "Beans"],
        "nutrient": "Iron"
    },
    "vitamin d": {
        "deficiency": "Low Vitamin D",
        "recommend": ["Sunlight", "Egg yolk", "Mushrooms", "Fatty fish"],
        "nutrient": "Vitamin D"
    },
    "wbc": {
        "deficiency": "White Blood Cells (WBC) Abnormality",
        "recommend": ["Garlic", "Yogurt", "Citrus fruits", "Broccoli"],
        "nutrient": "Immunity Support"
    },
    "cholesterol": {
        "deficiency": "High or Borderline Cholesterol",
        "recommend": ["Oats", "Almonds", "Avocados", "Olive Oil", "Green Tea", "Beans", "Fatty Fish"],
        "nutrient": "Heart Health"
    },
    "sodium": {
        "deficiency": "Sodium Abnormality Detected",
        "recommend": ["Bananas", "Sweet Potatoes", "Spinach", "Yogurt", "Beets"],
        "nutrient": "Blood Pressure Support"
    },
    "glucose": {
        "deficiency": "Glucose Abnormality Detected",
        "recommend": ["Leafy Greens", "Beans", "Nuts", "Oats", "Cinnamon"],
        "nutrient": "Blood Sugar Control"
    },
    "calcium": {
        "deficiency": "Low Calcium (Bone Health Risk)",
        "recommend": ["Milk", "Yogurt", "Cheese", "Almonds", "Broccoli"],
        "nutrient": "Bone Health"
    },
    "liver": {
        "deficiency": "Borderline Liver Enzymes (ALT, AST, SGPT)",
        "recommend": ["Turmeric", "Garlic", "Green Tea", "Leafy greens", "Beets"],
        "nutrient": "Liver Support"
    }
}

# 🧠 Phrase-Based Triggering for Safety
PHRASE_MAP = {
    "hemoglobin": ["low hemoglobin", "hemoglobin is low"],
    "iron": ["low iron", "iron deficiency", "iron is low"],
    "vitamin d": ["low vitamin d", "vitamin d deficiency"],
    "wbc": ["high wbc", "low wbc", "wbc abnormal", "wbc is elevated"],
    "cholesterol": ["high cholesterol", "cholesterol is high", "borderline cholesterol"],
    "sodium": ["high sodium", "low sodium", "sodium abnormal"],
    "glucose": ["high glucose", "low glucose", "glucose is elevated", "borderline glucose"],
    "calcium": ["low calcium", "calcium deficiency"],
    "liver": ["elevated alt", "high sgpt", "high ast", "borderline liver", "borderline alt", "borderline sgpt", "elevated liver enzymes"]
}


def get_nutrition_advice(text: str):
    """
    Scan input text for risky medical markers based on trigger phrases.
    """
    found = []
    lower_text = text.lower()

    for marker, phrases in PHRASE_MAP.items():
        if any(phrase in lower_text for phrase in phrases):
            advice = NUTRITION_MAP.get(marker)
            if advice:
                found.append(advice)

    return found


def plot_nutrient_chart(items):
    """
    Create a Plotly bar chart of food suggestions by nutrient.
    """
    nutrients = [item["nutrient"] for item in items]
    food_counts = [len(item["recommend"]) for item in items]

    fig = go.Figure([go.Bar(x=nutrients, y=food_counts)])
    fig.update_layout(title="Recommended Foods by Nutrient",
                      xaxis_title="Nutrient",
                      yaxis_title="No. of Recommended Foods")
    return fig
