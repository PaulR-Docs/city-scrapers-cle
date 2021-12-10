from city_scrapers_core.constants import ADVISORY_COMMITTEE, BOARD, SUBCOMMITTEE, FORUM
from city_scrapers_core.items import Meeting
from city_scrapers_core.spiders import CityScrapersSpider
from dateutil.relativedelata import relativedelta

class CuyaAdamhsMhracSpider(CityScrapersSpider):
    name = "cuya_adamhs_mhrac"
    agency = "Cuyahoga County ADAMHS"
    timezone = "America/Detroit"
    start_urls = ["https://www.adamhscc.org/about-us/current-initiatives/task-forces-and-coalitions/mental-health-response-advisory-committee-mhrac"]
    location = {"name": "Meetings held via Zoom", "address": "2012 W 25th St, 6th Floor Cleveland, OH 44113"}

  @property
def start_urls(self):
"""Start at calendar pages 2 months back and 2 months into the future"""

from city_scrapers_core.items import Meeting
from dateutil.relativedelta import relativedelta
  def parse(self, response):
        """
        `parse` should always `yield` Meeting items.

        Change the `_parse_title`, `_parse_start`, etc methods to fit your scraping
        needs.
        """
        table = response.xpath("//*[@id=\"events_widget_336_691_224\"]/div/table/tbody")
        rows = table.xpath('//tr')
        return_list =[]
        for item in rows:
             item=item.xpath(response.xpath("//*[@id=\"events_widget_336_691_224\"]/div/table/tbody/tr[1]/td[1]/a"))[0].extract()
             print (item)
             return_list.append(item)
        return return_list

def _parse_meeting(self, response):
"""Parse Meeting from detail page"""
  title = self._parse_title(response)
        meeting = Meeting(
            title=title,
            description="",
            classification=self._parse_classification(title),
            start=self._parse_start(response),
            end=self._parse_end(response),
            all_day=False,
            time_notes="",
            location=self._parse_location(response),
            links=self._parse_links(response),
            source=response.url,
    )

        meeting["status"] = self._get_status(
            meeting, text=response.css(".panel-flexible-inside")[0].extract()
        )
        meeting["id"] = self._get_id(meeting)

        yield meeting


#            meeting = Meeting(
#                title=self._parse_title(item),
#                description=self._parse_description(item),
#                classification=self._parse_classification(item),
#                start=self._parse_start(item),
#                end=self._parse_end(item),
#                all_day=self._parse_all_day(item),
#                time_notes=self._parse_time_notes(item),
#                location=self._parse_location(item),
#                links=self._parse_links(item),
#                source=self._parse_source(response),
#            )
#
#           meeting["status"] = self._get_status(meeting)
#           meeting["id"] = self._get_id(meeting)
#
#            yield meeting

    def _parse_title(self, item):
        """Parse or generate meeting title."""
        title_str = response.css("title_column event_title").extract_first().strip()
        if title_str == "Mental Health Response Advisory Committee (MHRAC) Meeting":
            return "Mental Health Response Advisory Committee Meeting (Full Committee)"
        if title_str == "MHRAC Diversion Subcommittee Meeting":
            return "MHRAC Diversion Subcommittee Meeting"
        if title_str == "MHRAC Community Engagement Subcommittee Meeting":
            return "MHRAC Community Engagement Subcommittee Meeting"
        if  title_str == "MHRAC QI Subcommittee Meeting":
	    return "MHRAC Quality Improvement Subcommittee Meeting"
        if title_str == "MHRAC Training Subcommittee Meeting":
            return "MHRAC Training Subcommittee Meeting"
        return re.sub(r" Meeting(s)?$", "", title_str)

    def _parse_description(self, item):
        """Parse or generate meeting description."""
	title_str = response.css("title_column event_title").extract_first().strip()
	if title_str == "Mental Health Response Advisory Committee (MHRAC) Meeting":
            return "About the MHRAC:
The Settlement Agreement between the City of Cleveland and the Department of Justice required that a Mental Health Response Advisory Committee (MHRAC) be developed by the City and the Cleveland Division of Police (CDP). The Committee is charged with: Fostering relationships and support between the police, community and mental health providers;
Identifying problems and developing solutions to improve crisis outcomes;
Providing guidance to improving, expanding and sustaining the CPD Crisis Intervention Program;
Conducting a yearly analysis of incidents to determine if the CPD has enough specialized CIT officers, if they are deployed effectively and responding appropriately and recommending changes to policies and procedures regarding training. "
        if title_str == "MHRAC Diversion Subcommittee Meeting":
            return "Diversion Subcommittee: Works with the Cleveland Division of Police to offer alternatives to the justice system for people with mental illness and addictions, such as diversion to hospitalization or treatment. "
        if title_str == "MHRAC Community Engagement Subcommittee Meeting":
            return "Community Involvement/Engagement Subcommittee: Fosters relationships between the Cleveland Police Department and the community by engaging the mental health and drug addiction community, police and the general public in meaningful dialogue that builds knowledge, sensitivity and understanding in order to inform and improve interactions and relationships through development of a plan to connect the general public, the police, and mental health and addiction specialists in each police district to build trust."
        if  title_str == "MHRAC QI Subcommittee Meeting":
            return "Quality Improvement Subcommittee: Reviews and discusses the data submitted from the CIT stat sheets and makes recommendations on ways to improve the quality and quantity of data collected in the reports.
"
        if title_str == "MHRAC Training Subcommittee Meeting":
            return "Training Subcommittee: Reviews and makes recommendations for 8-hour Mental Health/AoD training for all Cleveland Police officers and personnel, as well as the 40-hour CIT training for officers who volunteer for the training."
        return re.sub(r" Meeting Description?$", "", title_str)


    def _parse_classification(self, item):
        """Parse or generate classification from allowed options."""
        return NOT_CLASSIFIED

    def _parse_start(self, item):
        """Parse start datetime as a naive datetime object."""
        return None

    def _parse_end(self, item):
        """Parse end datetime as a naive datetime object. Added by pipeline if None"""
        return None

    def _parse_time_notes(self, item):
        """Parse any additional notes on the timing of the meeting"""
        return ""

    def _parse_all_day(self, item):
        """Parse or generate all-day status. Defaults to False."""
        return False

    def _parse_location(self, item):
        """Parse or generate location."""
        return {
            "address": "",
            "name": "",
        }

    def _parse_links(self, item):
        """Parse or generate links."""
        return [{"href": "", "title": ""}]

    def _parse_source(self, response):
        """Parse or generate source."""
        return response.url
