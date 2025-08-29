from dateutil import parser


class Parse:
    TIME_FORMAT = "%Y-%m-%d %H:%M"

    @staticmethod
    def time(x) -> str:
        x = x.replace("hrs", "")
        dt = parser.parse(x)
        return dt.strftime(Parse.TIME_FORMAT)
