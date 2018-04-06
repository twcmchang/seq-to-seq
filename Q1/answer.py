"""
Question 1: count selected candidates
"""

scores = [1, 10, 5, 3, 5]
lower_bounds = [0, 11, 2, 5]
upper_bounds = [5, 20, 9, 5]

def CountQualified(scores, lower_bounds, upper_bounds):
    """
    :param scores: A list of n candidate scores
    :param lower_bounds: A list of m lower bounds
    :param upper_bounds: A list of m upper bounds

    :return: A list of number of the qualified candidates given a pair of bounds
    
    Procedure
    :repeat the following step 1-3 for m pairs of upper bound and lower bound
        :step 1: for every score in a list: => O(n)
                     check whether that score is in the range of 
                     [lower bound, upper bound]  if yes, get 1; if not, get 0
        :step 2: sum up the results of this list => O(1)                                        
        :step 3: append to counts => O(1)                                                          

    Time complexity: O(mn)
    Space complexity: O(m)
    """
    counts = []
    for low, up in zip(lower_bounds, upper_bounds):
        assert up>=low, "an invalid pair of lower bound and upper bound [%s,%s]" % (low,up)
        counts.append(sum([1 if low <= num <= up else 0 for num in scores ]))
    return(counts)

if __name__ == '__main__':
    res = CountQualified(scores, lower_bounds, upper_bounds)
    print(res)
