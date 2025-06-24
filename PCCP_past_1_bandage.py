# [PCCP 기출문제] 1번 / 붕대 감기
# 해결

def solution(bandage, health, attacks):
    answer = 0

    # 시간
    time_ordinal = 1
    # 마지막 시간
    time_last_attack = attacks[-1][0] + 1
    # 연속 조건 번호
    sequence = 0
    # 최대 체력
    max_health = health
    # 빠른 조회위헤 공격의 사용 위치 기억(오름차순이기에 가능)
    i = 0

    while(time_ordinal != (time_last_attack)):
        if (time_ordinal == attacks[i][0]):
            health -= attacks[i][1]
            sequence = 0

            if (health <= 0):
                return -1
            
            i += 1

        else:
            sequence += 1
            if (health < max_health):
                if (health + bandage[1] > max_health):
                    health = max_health
                else:
                    health += bandage[1]

            if (sequence == bandage[0]):
                sequence = 0

                if (health < max_health):
                    if (health + bandage[2] > max_health):
                        health = max_health
                    else:
                        health += bandage[2]

        time_ordinal += 1

    answer = health
    return answer