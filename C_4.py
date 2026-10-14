#defining
def load_divider(vs, r1, r2, rl):
    v_unload = vs * (r2 / (r1 + r2))
    r_eq = (r2 * rl) / (r2 + rl)
    v_load = vs * (r_eq / (r1 + r_eq))
    return (v_unload, v_load)

result = load_divider(12, 1000, 1000, 500)
print("loaded_divider(12, 1000, 1000, 500) ->", result)
