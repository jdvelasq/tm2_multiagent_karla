from techminer2.database.tools import RecordViewer # type: ignore

viewer = (
    RecordViewer()
    #
    .where_root_directory_is("./")
    .where_database_is("main")
    .where_record_years_range_is(2015, None)
    .where_record_citations_range_is(None, None)
    .where_records_match({"document_type":["Review"]})
    .where_records_ordered_by("date_newest")

)
documents = viewer.run()


with open("./reports/reviews.txt", "w", encoding="utf-8") as f:
    for record in documents:
        f.write(f"{record}\n\n--\n\n")
        