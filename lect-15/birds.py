def new_sighting(kinds, counts, sighting):
    '''kinds: list of birds sighted so far
       counts: list of counts
       sighting: string (bird)
       function updates kinds and counts
        depending on sighting
    '''
    # if I have this bird before
    # then
    # find the index of sighting in kinds
    # add one to the counts at that index
    # else
    # append sighting to kinds
    # append 1 to counts
    if sighting in kinds:
        ind = kinds.index(sighting)
        counts[ind] = counts[ind] +1
    else:
        kinds.append(sighting)
        counts.append(1)


def new_sighting2(bird_dict, sighting):
    ''' bird_dict = {'falcon': 1, 'owl':5}
        sighting is a string (bird)
        update the bird_dict depending on
        the sighting
    '''
    if sighting in bird_dict:
        # update the count associated
        # with the key sighting
        bird_dict[sighting]+=1
    else:
        bird_dict[sighting] = 1
    
    

        
    
