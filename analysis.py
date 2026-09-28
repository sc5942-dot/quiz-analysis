from stats import mean_score

scores = [78, 85, 92, 64, 88]
passing = 70

avg = mean_score(scores)
print(f"Class average: {avg:.1f}")
n_pass = sum(s >= passing for s in scores)
print(f"Passed: {n_pass} of {len(scores)}")
