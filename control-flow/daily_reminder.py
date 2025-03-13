# طلب إدخال المهمة من المستخدم
task = input("Enter your task: ")

# طلب مستوى الأولوية
priority = input("Priority (high/medium/low): ")

# طلب ما إذا كانت المهمة مرتبطة بوقت محدد
time_bound = input("Is it time-bound? (yes/no): ")

# تعريف المتغير reminder مسبقًا
reminder = f"Reminder: '{task}' is a"

# استخدام Match Case لمعالجة الأولوية
match priority:
    case "high":
        reminder += " high priority task"
    case "medium":
        reminder += " medium priority task. Try to complete it soon."
    case "low":
        reminder += " low priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority entered."

# تعديل التذكير إذا كانت المهمة مرتبطة بوقت
if time_bound == "yes" and priority in ["high", "medium", "low"]:
    reminder += " that requires immediate attention today!"

# طباعة التذكير النهائي
print(reminder)
