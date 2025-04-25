# %%
import pandas as pd  # type: ignore
from techminer2.database.metrics.general import DataFrame  # type: ignore

df = (
    DataFrame()
    #
    # DATABASE:
    .where_root_directory_is("../")
    .where_database_is("main")
    .where_record_years_range_is(2015, 2024)
    .where_record_citations_range_is(None, None)
    .where_records_match(
        {
            "document_type": [
                'Article',
                'Book',
                'Book chapter',
                'Conference paper',
                'Conference review',
                'Editorial',
                'Review',
            ]
        }
    )
    .run()
)
df

# %%
