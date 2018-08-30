import pprint, requests

class CSSScraper:
    def manage_internal(in_text):
        if in_text.count('{') and in_text.count('}'):
            return in_text
        else:
            if in_text.count(';'):
                all_split_text = in_text.split(';')
                internal_dict = {}
                for text in all_split_text:
                    single_split_text = text.split(':')
                    internal_dict.update({(single_split_text[0]).strip():(single_split_text[1]).strip()})
                return internal_dict
            else:
                single_split_text = in_text.split(':')
                if not ((len(single_split_text) == 0) or (len(single_split_text) == 1)):
                    return {(single_split_text[0]).strip():(single_split_text[1]).strip()}

    def css_test(s):
        in_text = ''
        out_text = ''
        d = {}
        is_in = False
        for i in range(len(s)):
            if s[i] == '}':
                is_in = False
                out_text = out_text.replace('{','')
                out_text = out_text.replace('}','')
                d.update({out_text:in_text})
                in_text = ''
                out_text = ''
            if is_in:
                in_text = in_text + s[i]
            else:
                out_text = out_text + s[i]
            if s[i] == '{':
                is_in = True

        for i in d.keys():
            d.update({i:manage_internal(d[i])})
        return d
