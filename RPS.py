def player(prev_play, opponent_history=[], play_order={}):
    # If this is the first play (no previous play), set the default to 'R'
    if not prev_play:
        prev_play = 'R'

    # Record the previous play in the opponent's history
    opponent_history.append(prev_play)
    # Default prediction is 'P' (Paper)
    prediction = 'P'

    # If we have more than 4 plays in history, analyze patterns
    if len(opponent_history) > 4:
        # Create a string of the last 5 plays
        last_five = "".join(opponent_history[-5:])
        
        # Update the play_order dictionary with the frequency of this pattern
        play_order[last_five] = play_order.get(last_five, 0) + 1
        
        # Generate possible patterns for the next play
        potential_plays = [
            "".join([*opponent_history[-4:], v]) 
            for v in ['R', 'P', 'S']
        ]

        # Filter play_order to include only patterns that have been seen
        sub_order = {
            k: play_order[k]
            for k in potential_plays if k in play_order
        }

        # If we have any known patterns, choose the most frequent one
        if sub_order:
            # Select the most frequent next play based on historical patterns
            prediction = max(sub_order, key=sub_order.get)[-1:]

    # Define the ideal response for each possible play
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    # Return the response that beats the predicted next play
    return ideal_response[prediction]
