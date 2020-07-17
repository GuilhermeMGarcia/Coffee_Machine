exercito = int(input())

if exercito < 1:
    print('no army')
elif (exercito >= 1) and (exercito <= 9):
    print('few')
elif (exercito >= 10) and (exercito <= 49):
    print('pack')
elif (exercito >= 50) and (exercito <= 499):
    print('horde')
elif (exercito >= 500) and (exercito <= 999):
    print('swarm')
else:
    print('legion')