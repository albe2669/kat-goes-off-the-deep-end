from subprocess import Popen, PIPE


def query_simulator(query, dims, box):
    H, W = dims
    br, bc = box
    cmd = ["python3", "simulator.py", f"{H} {W}", f"{br} {bc}"]
    simulator = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE)
    assert simulator.stdout and simulator.stdin
    return send(simulator, query)


def read_line(target):
    return str(target.stdout.readline(), encoding="utf-8")


def send(target, data):
    target.stdin.write(bytes(data, encoding="utf-8"))
    target.stdin.flush()
    return read_line(target)


def test(dims, box):
    solution = Popen(["python3", "findthebox.py"],
                     stdout=PIPE, stdin=PIPE, stderr=PIPE)

    assert solution.stdout and solution.stdin, "Failed to open pipes"

    dims_data = f"{dims[0]} {dims[1]}\n"

    first_query = send(solution, dims_data)
    first_pos = query_simulator(first_query, dims, box)
    second_query = send(solution, first_pos)

    if second_query.startswith("!"):
        return second_query.strip()

    second_pos = query_simulator(second_query, dims, box)
    answer = send(solution, second_pos)

    return answer.strip()


if __name__ == "__main__":
    for h in range(5, 10):
        for w in range(5, 10):
            if h == 1 and w == 1:
                continue

            for r in range(h):
                for c in range(w):
                    if r == 0 and c == 0:
                        continue


                    case = f"{h} x {w} with box in ({r}, {c})"
                    print(f"Testing {case}")
                    answer = test((h, w), (r, c))

                    if answer != f"! {r} {c}":
                        print(f"Failed for {case}")
                        print(f"Expected {r} {c}, got {answer}")
                        exit(1)
