  
import requests

states = ['PA', 'NC', 'GA', 'NV', 'AZ']

for state in states:

    url = f'https://politics-elex-results.data.api.cnn.io/results/view/2020-county-races-PG-{state}.json'

    state_date = requests.get(url).json()

    biden = 0
    trump = 0

    biden_project = 0
    trump_project = 0

    for county in state_date:
        biden_vote = 0
        trump_vote = 0
        
        percent_reporting = county['percentReporting']
        
        for candidate in county['candidates']:
            candidate_name = candidate['lastName']
            candidate_vote = candidate['voteNum']
            if candidate_name == 'Biden':
                biden_vote = candidate_vote

            if candidate_name == 'Trump':
                trump_vote = candidate_vote

        if percent_reporting < 100 and percent_reporting > 0:

            biden_project = (biden_vote * 100) / (percent_reporting) 
            trump_project = (trump_vote * 100) / (percent_reporting) 

            biden += biden_project
            trump += trump_project

        else:

            biden += biden_vote
            trump += trump_vote


    print()
    print(state)
    if biden > trump:
        print('Biden', int((biden - trump)))
    else:
        print('Trump', int((trump - biden)))    
