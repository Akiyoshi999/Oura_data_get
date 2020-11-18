# -*- coding: utf-8 -*-
split_line = '\n===============\n'

def score_create(today_scores, week_scores):
    '''
    スコアをメッセージにするモジュール
    '''
    message = None
    week_score = None
    today_score = ('本日のスコア\n' + '\n'.join\
                    (['{:12} = {:5}'.format(k, v) for k, v in today_scores.items()]))
    if week_scores:
        week_score = ('1週間の平均スコア\n' + '\n'.join\
                    (['{:1} = {:5}'.format(k, v) for k, v in week_scores.items()]))
        message = split_line + today_score + split_line + week_score
    else:
        message = split_line + today_score
    return message


def blurred_create(today_score):
    '''
    ぼやきメッセージを作成する
    スコアが悪ければ、その悪いスコアを教えるメッセージを作成する
    '''
    bad_item = []
    blurred_message = None

    for key, value in today_score.items():
        if key == 'active' and value <= 49:
            bad_item.append(key)
        elif value <= 69:
            bad_item.append(key)
    if bad_item is None:
        blurred_message = ('本日はの体調は良好です')
    else:
        blurred_message = ('今日は' + ', '.join(bad_item) + 'が不調みたい。')
    return split_line + blurred_message
