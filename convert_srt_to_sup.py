import pysrt
import csv

subs = pysrt.open('lastdownloaded_converted.srt')


with open("out.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerow(
            ("Start",
             "End",
             "Character",
             "Original Text",
             "Translation",
             "Machine Translations"))
        for caption in subs:
                writer.writerow(
                    (caption.start,
                     caption.end,
                     "",
                     caption.text,
                     "",
                     ""))
                print "%s s:%s e:%s" % (caption.text.replace('\n', ' ')
                .replace('\r', ''), caption.start, caption.end)
