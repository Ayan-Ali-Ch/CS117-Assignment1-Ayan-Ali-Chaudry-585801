def star_to_delta(ra, rb, rc):
    r_num = (ra * rb) + (rb * rc) + (rc * ra)
    rab = r_num / rc
    rbc = r_num / ra
    rca = r_num / rb
    return (round(rab, 2), round(rbc, 2), round(rca, 2))

result = star_to_delta(10, 20, 30)
print("star_to_delta(10, 20, 30) ->", result)
