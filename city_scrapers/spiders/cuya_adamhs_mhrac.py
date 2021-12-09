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
        return ""

    def _parse_description(self, item):
        """Parse or generate meeting description."""
        return ""

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
