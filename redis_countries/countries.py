import sys
import csv
import redis


class RedisCountries():

    def __init__(self, r='localhost'):
        if isinstance(r, redis.client.Redis):
            self.redis = r
        elif isinstance(r, dict):
            self.redis = redis.Redis(**r)
        else:
            self.redis = redis.Redis(r)

    def _geoip_redis_aton(self, ip):
        """Convert string string IP to integer representation."""
        try:
            x = map(int, ip.split('.'))
            return (x[0] << 24) | (x[1] << 16) | (x[2] << 8) | (x[3] << 0)
        except:
            return None

    def download_data(self):
        """Downloads the database file from MaxMind's website."""
        pass

    def import_data(self, filename):
        """Read each line of the csv file and import it as a redis record."""
        with open(filename, 'r') as f:
            file_reader = csv.reader(f)
            for row_index, data in enumerate(file_reader):
                if len(data) != 6:
                    print "Malformed line, skipping..."
                    continue
                num_start, num_end, country_code, country = data[2:]
                key = country_code + ":" + str(row_index)
                self.redis.zadd("geoip", key + ":s", num_start)
                self.redis.zadd("geoip", key + ":e", num_end)


    def get_country_code(self, ip, default_country=None):
        """Lookup ip and return the country code or None."""

        ipnum = self._geoip_redis_aton(ip)
        if not ipnum:
            return default_country
        result = self.redis.zrangebyscore("geoip", ipnum, 'inf',
                                           0, 1, withscores=True)
        if not result:
            return default_country

        res, score = result[0]
        parts = res.split(":")
        if len(parts) != 3:
            return default_country
        country_code = parts[0]
        start_end = parts[2]
        if start_end == "s":
            if float(score) > ipnum:
                # We have the start of a new block and IP actually is not found
                return default_country
        return country_code


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Please specify csv file containing the data.")
    ipc = IPCountries()
    ipc.import_data(sys.argv[1])
