from line_bot_api import *
from linebot.models import *

def res_1(event):
    import pymysql
    userid = event.source.user_id
    db = pymysql.connect(host="54.65.74.214",
                         user="root",
                         password="password",
                         db="demo",
                         port=3306,
                         charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute('''select count(*) from demo.user_history_test1 where user_id=('%s')'''%(userid))
    data = cursor.fetchone()
    if data['count(*)'] == 0:
        carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(

                        title='食物偏好',
                        text='Please select service',
                        actions=[
                            PostbackAction(
                                label='高',
                                display_text='高',
                                data='A&5'

                            ),
                            PostbackAction(
                                label='中',
                                display_text='中',
                                data='A&3'
                            ), PostbackAction(
                                label='低',
                                display_text='低',
                                data='A&1'

                            )

                        ]
                    )
                ]
            )
        )


        line_bot_api.reply_message(
            reply_token=event.reply_token,
            messages=[
                carousel_template_message]
        )

        @handler.add(PostbackEvent)
        def handle_postback(event):

            if event.postback.data[0:1] == "A":
                food_= event.postback.data[2:]
                carousel_template_message = TemplateSendMessage(
                    alt_text='Carousel template',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(

                                title='服務偏好',
                                text='Please select service',
                                actions=[
                                    PostbackAction(
                                        label='高',
                                        display_text='高',
                                        data='B&5'

                                    ),
                                    PostbackAction(
                                        label='中',
                                        display_text='中',
                                        data='B&3'
                                    ), PostbackAction(
                                        label='低',
                                        display_text='低',
                                        data='B&1'

                                    )

                                ]
                            )
                        ]
                    )
                )

                line_bot_api.reply_message(
                    reply_token=event.reply_token,
                    messages=[
                        carousel_template_message]
                )

                @handler.add(PostbackEvent)
                def handle_postback(event):

                    if event.postback.data[0:1] == "B":
                        ser_ = event.postback.data[2:]
                        carousel_template_message = TemplateSendMessage(
                            alt_text='Carousel template',
                            template=CarouselTemplate(
                                columns=[
                                    CarouselColumn(

                                        title='實惠偏好',
                                        text='Please select service',
                                        actions=[
                                            PostbackAction(
                                                label='高',
                                                display_text='高',
                                                data='C&5'

                                            ),
                                            PostbackAction(
                                                label='中',
                                                display_text='中',
                                                data='C&3'
                                            ), PostbackAction(
                                                label='低',
                                                display_text='低',
                                                data='C&1'

                                            )

                                        ]
                                    )
                                ]
                            )
                        )

                        line_bot_api.reply_message(
                            reply_token=event.reply_token,
                            messages=[
                                carousel_template_message]
                        )

                        @handler.add(PostbackEvent)
                        def handle_postback(event):

                            if event.postback.data[0:1] == "C":
                                cp_ = event.postback.data[2:]
                                carousel_template_message = TemplateSendMessage(
                                    alt_text='Carousel template',
                                    template=CarouselTemplate(
                                        columns=[
                                            CarouselColumn(

                                                title='環境偏好',
                                                text='Please select service',
                                                actions=[
                                                    PostbackAction(
                                                        label='高',
                                                        display_text='高',
                                                        data='D&5'

                                                    ),
                                                    PostbackAction(
                                                        label='中',
                                                        display_text='中',
                                                        data='D&3'
                                                    ), PostbackAction(
                                                        label='低',
                                                        display_text='低',
                                                        data='D&1'

                                                    )

                                                ]
                                            )
                                        ]
                                    )
                                )

                                line_bot_api.reply_message(
                                    reply_token=event.reply_token,
                                    messages=[
                                        carousel_template_message]
                                )

                                @handler.add(PostbackEvent)
                                def handle_postback(event):

                                    if event.postback.data[0:1] == "D":
                                        env_ = event.postback.data[2:]
                                        questionnaire = [int(food_), int(ser_), int(cp_), int(env_)]
                                        print(questionnaire)




    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='有會員'))
    cursor.close()
