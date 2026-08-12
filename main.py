import os
import json
from datetime import date
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

TIPS = [
    "ابدأ يومك بخطوة صغيرة، النجاح يبدأ بالاستمرارية.",
    "لا تقارن نفسك بالآخرين، قارن نفسك بالأمس.",
    "الراحة الحقيقية تأتي بعد إنجاز حقيقي.",
    "كل يوم فرصة جديدة، لا تضيعها بالتردد.",
    "النظام يهزم الحافز، ابنِ عادات لا تعتمد على مزاجك.",
    "خطوة بطيئة للأمام أفضل من وقوف طويل.",
    "ثقتك بنفسك تُبنى بالأفعال لا بالكلام.",
    "لا تخف من الفشل، خف من عدم المحاولة.",
    "راجع أهدافك كل أسبوع، وعدّل مسارك عند الحاجة.",
    "استثمر وقتك في تطوير نفسك، فهو أفضل استثمار."
]

TASKS = [
    "اكتب 3 أهداف تريد تحقيقها اليوم.",
    "مارس الرياضة 15 دقيقة على الأقل.",
    "اقرأ 10 صفحات من كتاب مفيد.",
    "تواصل مع شخص يهمك أمره.",
    "رتب مكان عملك أو غرفتك.",
    "اكتب 3 أشياء تشعر بالامتنان لها.",
    "خطط ليومك التالي قبل النوم."
]

DATA_FILE = "mxdata.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    data = {"start_date": str(date.today())}
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
    return data

def day_index(start_date_str, length):
    start = date.fromisoformat(start_date_str)
    days_passed = (date.today() - start).days
    return days_passed % length

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=20, **kwargs)
        self.build_ui()

    def build_ui(self):
        self.clear_widgets()
        data = load_data()
        tip = TIPS[day_index(data["start_date"], len(TIPS))]
        task = TASKS[day_index(data["start_date"], len(TASKS))]

        self.add_widget(Label(text="MX - معلمك الشخصي", font_size=30))
        self.add_widget(Label(text=f"نصيحة اليوم:\n{tip}", font_size=20))
        self.add_widget(Label(text=f"مهمة اليوم:\n{task}", font_size=20))

        refresh_btn = Button(text="تحديث", size_hint=(1, 0.3))
        refresh_btn.bind(on_press=lambda x: self.build_ui())
        self.add_widget(refresh_btn)

class MXApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    MXApp().run()
