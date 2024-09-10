from g4f.client import Client
import re


def chat_with_gpt(user_id, text_chatGPT_35_turbo):
    try:
        system_message = {
            "role": "system",
            "content": "You are an assistant who extracts (Name, Age, Gender, Occupation, Marital Status, Number of Children, Education Level, Location, Nationality, Languages Spoken) from the given text and wrote it at the front output of each word label."
        }
        user_message = {"role": "user", "content": text_chatGPT_35_turbo}

        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[system_message, user_message],  # Only current conversation messages
            temperature=0.5,  # Adjusts creativity vs accuracy
            max_tokens=50,   # Limits the response length
            top_p=0.9,        # Controls diversity of responses
            frequency_penalty=0.5,  # Reduces repetition
            presence_penalty=0.6     # Encourages new topic introduction
        )

        model_reply = response.choices[0].message.content
        return model_reply
    except Exception as e:
        print(f"An error occurred: {e}")
        return "متاسفانه یک خطا رخ داده است، لطفا دوباره تلاش کنید."




# تابع برای خواندن فایل Specifications.txt و جایگذاری اطلاعات
def update_specifications(file_name, profile_data):
    # خواندن فایل Specifications.txt
    with open(file_name, 'r') as file:
        content = file.readlines()

    # استخراج اطلاعات از personal_profile
    profile_dict = {}
    for line in profile_data.split("\n"):
        if ": " in line:
            key, value = line.split(": ", 1)
            profile_dict[key.strip().lower()] = value.strip()

    # جایگذاری اطلاعات در فایل Specifications.txt
    updated_content = []
    for line in content:
        # پیدا کردن لیبل‌ها (مثال: 1_name:) و استخراج کلید
        match = re.match(r"(\d+)_(.+?):\s*(.*)", line)
        if match:
            label_number = match.group(1)
            label = match.group(2).strip().replace("_", " ").lower()
            existing_value = match.group(3).strip()

            # اگر جلوی لیبل مقدار وجود نداشت و در پروفایل کلید مربوطه موجود بود، مقدار را جایگذاری کن
            if not existing_value and label in profile_dict:
                updated_content.append(f"{label_number}_{label}: {profile_dict[label]}\n")
            else:
                # اگر قبلاً مقداری وجود دارد، همان خط را بدون تغییر اضافه کن
                updated_content.append(line)
        else:
            updated_content.append(line)

    # نوشتن محتوای به روز شده به فایل Specifications.txt
    with open(file_name, 'w') as file:
        file.writelines(updated_content)


        
personal_profile = chat_with_gpt("user_id", "My name is John Doe, I'm 35 years old, male, working as a software engineer. I'm married and have 2 children. I live in New York, and I'm American. I speak English and French.")
print(personal_profile)

update_specifications('Specifications.txt', personal_profile)
