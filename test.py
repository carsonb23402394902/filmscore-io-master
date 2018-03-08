import boxofficemojoAPI as bom

box_office_mojo = bom.BoxOfficeMojo()
box_office_mojo.crawl_for_urls()


movie = box_office_mojo.get_movie_summary("titanic")
movie.clean_data()
print movie.to_json()

weekly = box_office_mojo.get_weekly_summary("titanic")
weekly.clean_data()
print weekly.to_json()
