import json


async def getServerVar(args, Context):
    from CharmCord.Classes.CharmCord import all_vars
    ag = args.split(";")
    server = ag[0]
    var = ag[1]
    try:
        with open("variables.json", "r") as vars:
            total = json.load(vars)
            return total[f"{server}_{var}"]
    except KeyError:
        with open("variables.json", "r") as vars:
            total = json.load(vars)
        with open("variables.json", "w") as vars:
            total.update({f"{server}_{var}": all_vars[var]})
            json.dump(total, vars)
            return all_vars[var]