import ast


def single_quoted_json_to_dict(path: str) -> dict:
    with open(path) as f:
        return ast.literal_eval(f.read())


if __name__ == "__main__":
    data = single_quoted_json_to_dict("result.txt")
    desc = data["vulnerabilities"][0]["cve"]["descriptions"]
    print(desc)
