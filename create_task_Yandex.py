from yandex_tracker_client import TrackerClient

#создаем запрос к трекеру
client = TrackerClient(token='y0_AgAAAAA-3GsuAAr94wAAAAD0xSckgHxfHpdnQwCmO3Ad1qpH1RY3wMM', cloud_org_id='bpfmgj2hpqfr8vcthm75')

#запрашиваем очередь
queue = client.queues['TEAMCITYBUILDF']
#получаем владельца
manager = queue.lead
#создаем задачу с типом "Ошибка"

main_issue = client.issues.create(
        queue='TEAMCITYBUILDF',
        assignee=manager,
        type={'name': 'Bug'},
        summary='Build Failed',
        description='Build from TeamCity Failed'
    )
    #назначаем отслеживающих
followers = ['catherinedots']
main_issue.update(followers={'add': followers})
