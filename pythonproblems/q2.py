# q2


# defining required function
def bal(ccn):
    if len(ccn) == 16:
        return "Your credit card " + "************" + ccn[-4:] + " has a balance of XX rupees."
    elif len(ccn) != 16:
        return "Invalid input"

# checked
