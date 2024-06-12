

import requests
import json
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from database import get_news_by_category

def get_category_vietnamnet():
    with open('categories.txt', 'r', encoding='utf-8') as f:
        categories = f.read().splitlines()
        # tạo thành 1 string Thị trường, Chính trị, Thời sự, Tài chính, Thể thao, Giải trí, Khoa học, Công nghệ, Sức khỏe, Thời tiết
        categories = ', '.join(categories)
    return categories

def chat(question):
    url = "https://api.openai.com/v1/chat/completions"

    payload = json.dumps({
    "model": "gpt-3.5-turbo-1106",
    "messages": [
        {
        "role": "system",
        # flex cho phần này, muốn custom thì custom thêm vào đây
        "content": f"""Bạn là model nhận dạng label câu hỏi và trả về thông tin 1 trong loại sau đây, không thêm bớt ({get_category_vietnamnet()}). 
        Bạn là chatbot tổng hợp tin tức được phát triển bởi Trần Anh Minh,tin tức được cập nhật đến thời điểm ngày {time.strftime('%d/%m/%Y')}"""
        },
        {
        "role": "user",
        "content": "Tôi muốn xem tin tức về chính trị"
        },
        {
            "role": "assistant",
            "content": "Chính trị"
        },
        {
            "role": "user",
            "content": "Tin tức thời tiết hôm nay"
        },
        {
            "role": "assistant",
            "content": "Thời tiết"
        },
        {
            "role": "user",
            "content": "tin tức kinh tế hôm nay"
        },
        {
            "role": "assistant",
            "content": "Tài chính"
        },
        {
            "role": "user",
            "content": question
        }
    ],
    "max_tokens": 400,
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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',
    'Cookie': '__cf_bm=_AszksyNOpPVN_i1vNOc4xSee9hdzBUX37wUKilP9aI-1717624296-1.0.1.1-a9IQjuhpmnrUrhWjraMAKg9FXQlPnbKHvjhN.zIsUhoD6YQ8pi3EK2wg7OqmvLH3xY5P2pV0j92fthgjJ6cHVw; _cfuvid=aPGAuu6R06CeamL.vUb22.rshQZl7mwjMalPUMAlG9I-1717620820919-0.0.1.1-604800000'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    text = response.json()['choices'][0]['message']['content']

    return text


def get_list_categories():
    with open('categories.txt', 'r', encoding='utf-8') as f:
        categories = f.read().strip().splitlines()
    return categories

    

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if len(text) > 200:
        await update.message.reply_text("Tin nhắn quá dài, hãy nói ngắn gọn hơn!")
    answer = chat(text)
    if answer in get_list_categories():
        messages = get_news_by_category(answer)
        if len(messages) == 0:
            await update.message.reply_text(f"Có vẻ như không có tin tức nào về {answer}!")
        else:
            await update.message.reply_text(f"Hôm nay có {len(messages)} bài báo về {answer}!")
            for i, message in enumerate(messages):
                
                url = f"https://vietnamnet.vn{message['url']}"
                # tạo 1 tin nhắn với nội dung là title in đậm, description, kèm upload ảnh, kèm link đến bài báo 
                await update.message.reply_text(f"<b>{i+1}. {message['title']}</b>\n{url}\n{message['description']}", parse_mode='HTML')
    else:
        await update.message.reply_text(answer)

app = ApplicationBuilder().token("7282533045:AAE5qWYftSDdaQCxCVPeMv_G2u1qFiUg-U0").build()

# Thêm MessageHandler để xử lý tất cả các tin nhắn văn bản
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), reply))

app.run_polling()
    
    
