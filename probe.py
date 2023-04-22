from datetime import datetime
from typing import Any, Optional, Dict, List, TypeVar, Type, cast, Callable
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_stringified_bool(x: str) -> bool:
    if x == "true":
        return True
    if x == "false":
        return False
    assert False


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return {k: f(v) for (k, v) in x.items()}


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class FormatTags:
    encoder: str
    creation_time: datetime

    def __init__(self, encoder: str, creation_time: datetime) -> None:
        self.encoder = encoder
        self.creation_time = creation_time

    @staticmethod
    def from_dict(obj: Any) -> 'FormatTags':
        assert isinstance(obj, dict)
        encoder = from_str(obj.get("encoder"))
        creation_time = from_datetime(obj.get("creation_time"))
        return FormatTags(encoder, creation_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["encoder"] = from_str(self.encoder)
        result["creation_time"] = self.creation_time.isoformat()
        return result


class Format:
    filename: str
    nb_streams: int
    nb_programs: int
    format_name: str
    format_long_name: str
    start_time: str
    duration: str
    size: str
    bit_rate: int
    probe_score: int
    tags: FormatTags

    def __init__(self, filename: str, nb_streams: int, nb_programs: int, format_name: str, format_long_name: str, start_time: str, duration: str, size: str, bit_rate: int, probe_score: int, tags: FormatTags) -> None:
        self.filename = filename
        self.nb_streams = nb_streams
        self.nb_programs = nb_programs
        self.format_name = format_name
        self.format_long_name = format_long_name
        self.start_time = start_time
        self.duration = duration
        self.size = size
        self.bit_rate = bit_rate
        self.probe_score = probe_score
        self.tags = tags

    @staticmethod
    def from_dict(obj: Any) -> 'Format':
        assert isinstance(obj, dict)
        filename = from_str(obj.get("filename"))
        nb_streams = from_int(obj.get("nb_streams"))
        nb_programs = from_int(obj.get("nb_programs"))
        format_name = from_str(obj.get("format_name"))
        format_long_name = from_str(obj.get("format_long_name"))
        start_time = from_str(obj.get("start_time"))
        duration = from_str(obj.get("duration"))
        size = from_str(obj.get("size"))
        bit_rate = int(from_str(obj.get("bit_rate")))
        probe_score = from_int(obj.get("probe_score"))
        tags = FormatTags.from_dict(obj.get("tags"))
        return Format(filename, nb_streams, nb_programs, format_name, format_long_name, start_time, duration, size, bit_rate, probe_score, tags)

    def to_dict(self) -> dict:
        result: dict = {}
        result["filename"] = from_str(self.filename)
        result["nb_streams"] = from_int(self.nb_streams)
        result["nb_programs"] = from_int(self.nb_programs)
        result["format_name"] = from_str(self.format_name)
        result["format_long_name"] = from_str(self.format_long_name)
        result["start_time"] = from_str(self.start_time)
        result["duration"] = from_str(self.duration)
        result["size"] = from_str(self.size)
        result["bit_rate"] = from_str(str(self.bit_rate))
        result["probe_score"] = from_int(self.probe_score)
        result["tags"] = to_class(FormatTags, self.tags)
        return result


class StreamTags:
    language: str
    bps_eng: int
    duration_eng: datetime
    number_of_frames_eng: int
    number_of_bytes_eng: str
    statistics_writing_app_eng: str
    statistics_writing_date_utc_eng: datetime
    statistics_tags_eng: str
    title: Optional[str]

    def __init__(self, language: str, bps_eng: int, duration_eng: datetime, number_of_frames_eng: int, number_of_bytes_eng: str, statistics_writing_app_eng: str, statistics_writing_date_utc_eng: datetime, statistics_tags_eng: str, title: Optional[str]) -> None:
        self.language = language
        self.bps_eng = bps_eng
        self.duration_eng = duration_eng
        self.number_of_frames_eng = number_of_frames_eng
        self.number_of_bytes_eng = number_of_bytes_eng
        self.statistics_writing_app_eng = statistics_writing_app_eng
        self.statistics_writing_date_utc_eng = statistics_writing_date_utc_eng
        self.statistics_tags_eng = statistics_tags_eng
        self.title = title

    @staticmethod
    def from_dict(obj: Any) -> 'StreamTags':
        assert isinstance(obj, dict)
        language = from_str(obj.get("language"))
        bps_eng = int(from_str(obj.get("BPS-eng")))
        duration_eng = from_datetime(obj.get("DURATION-eng"))
        number_of_frames_eng = int(from_str(obj.get("NUMBER_OF_FRAMES-eng")))
        number_of_bytes_eng = from_str(obj.get("NUMBER_OF_BYTES-eng"))
        statistics_writing_app_eng = from_str(
            obj.get("_STATISTICS_WRITING_APP-eng"))
        statistics_writing_date_utc_eng = from_datetime(
            obj.get("_STATISTICS_WRITING_DATE_UTC-eng"))
        statistics_tags_eng = from_str(obj.get("_STATISTICS_TAGS-eng"))
        title = from_union([from_str, from_none], obj.get("title"))
        return StreamTags(language, bps_eng, duration_eng, number_of_frames_eng, number_of_bytes_eng, statistics_writing_app_eng, statistics_writing_date_utc_eng, statistics_tags_eng, title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["language"] = from_str(self.language)
        result["BPS-eng"] = from_str(str(self.bps_eng))
        result["DURATION-eng"] = self.duration_eng.isoformat()
        result["NUMBER_OF_FRAMES-eng"] = from_str(
            str(self.number_of_frames_eng))
        result["NUMBER_OF_BYTES-eng"] = from_str(self.number_of_bytes_eng)
        result["_STATISTICS_WRITING_APP-eng"] = from_str(
            self.statistics_writing_app_eng)
        result["_STATISTICS_WRITING_DATE_UTC-eng"] = self.statistics_writing_date_utc_eng.isoformat()
        result["_STATISTICS_TAGS-eng"] = from_str(self.statistics_tags_eng)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        return result


class Stream:
    index: int
    codec_name: str
    codec_long_name: str
    profile: Optional[str]
    codec_type: str
    codec_tag_string: str
    codec_tag: str
    width: Optional[int]
    height: Optional[int]
    coded_width: Optional[int]
    coded_height: Optional[int]
    closed_captions: Optional[int]
    film_grain: Optional[int]
    has_b_frames: Optional[int]
    sample_aspect_ratio: Optional[str]
    display_aspect_ratio: Optional[str]
    pix_fmt: Optional[str]
    level: Optional[int]
    color_range: Optional[str]
    color_space: Optional[str]
    chroma_location: Optional[str]
    field_order: Optional[str]
    refs: Optional[int]
    is_avc: Optional[bool]
    nal_length_size: Optional[int]
    r_frame_rate: str
    avg_frame_rate: str
    time_base: str
    start_pts: int
    start_time: str
    bits_per_raw_sample: Optional[int]
    extradata_size: Optional[int]
    disposition: Dict[str, int]
    tags: StreamTags
    sample_fmt: Optional[str]
    sample_rate: Optional[int]
    channels: Optional[int]
    channel_layout: Optional[str]
    bits_per_sample: Optional[int]
    bit_rate: Optional[int]

    def __init__(self, index: int, codec_name: str, codec_long_name: str, profile: Optional[str], codec_type: str, codec_tag_string: str, codec_tag: str, width: Optional[int], height: Optional[int], coded_width: Optional[int], coded_height: Optional[int], closed_captions: Optional[int], film_grain: Optional[int], has_b_frames: Optional[int], sample_aspect_ratio: Optional[str], display_aspect_ratio: Optional[str], pix_fmt: Optional[str], level: Optional[int], color_range: Optional[str], color_space: Optional[str], chroma_location: Optional[str], field_order: Optional[str], refs: Optional[int], is_avc: Optional[bool], nal_length_size: Optional[int], r_frame_rate: str, avg_frame_rate: str, time_base: str, start_pts: int, start_time: str, bits_per_raw_sample: Optional[int], extradata_size: Optional[int], disposition: Dict[str, int], tags: StreamTags, sample_fmt: Optional[str], sample_rate: Optional[int], channels: Optional[int], channel_layout: Optional[str], bits_per_sample: Optional[int], bit_rate: Optional[int]) -> None:
        self.index = index
        self.codec_name = codec_name
        self.codec_long_name = codec_long_name
        self.profile = profile
        self.codec_type = codec_type
        self.codec_tag_string = codec_tag_string
        self.codec_tag = codec_tag
        self.width = width
        self.height = height
        self.coded_width = coded_width
        self.coded_height = coded_height
        self.closed_captions = closed_captions
        self.film_grain = film_grain
        self.has_b_frames = has_b_frames
        self.sample_aspect_ratio = sample_aspect_ratio
        self.display_aspect_ratio = display_aspect_ratio
        self.pix_fmt = pix_fmt
        self.level = level
        self.color_range = color_range
        self.color_space = color_space
        self.chroma_location = chroma_location
        self.field_order = field_order
        self.refs = refs
        self.is_avc = is_avc
        self.nal_length_size = nal_length_size
        self.r_frame_rate = r_frame_rate
        self.avg_frame_rate = avg_frame_rate
        self.time_base = time_base
        self.start_pts = start_pts
        self.start_time = start_time
        self.bits_per_raw_sample = bits_per_raw_sample
        self.extradata_size = extradata_size
        self.disposition = disposition
        self.tags = tags
        self.sample_fmt = sample_fmt
        self.sample_rate = sample_rate
        self.channels = channels
        self.channel_layout = channel_layout
        self.bits_per_sample = bits_per_sample
        self.bit_rate = bit_rate

    @staticmethod
    def from_dict(obj: Any) -> 'Stream':
        assert isinstance(obj, dict)
        index = from_int(obj.get("index"))
        codec_name = from_str(obj.get("codec_name"))
        codec_long_name = from_str(obj.get("codec_long_name"))
        profile = from_union([from_str, from_none], obj.get("profile"))
        codec_type = from_str(obj.get("codec_type"))
        codec_tag_string = from_str(obj.get("codec_tag_string"))
        codec_tag = from_str(obj.get("codec_tag"))
        width = from_union([from_int, from_none], obj.get("width"))
        height = from_union([from_int, from_none], obj.get("height"))
        coded_width = from_union([from_int, from_none], obj.get("coded_width"))
        coded_height = from_union(
            [from_int, from_none], obj.get("coded_height"))
        closed_captions = from_union(
            [from_int, from_none], obj.get("closed_captions"))
        film_grain = from_union([from_int, from_none], obj.get("film_grain"))
        has_b_frames = from_union(
            [from_int, from_none], obj.get("has_b_frames"))
        sample_aspect_ratio = from_union(
            [from_str, from_none], obj.get("sample_aspect_ratio"))
        display_aspect_ratio = from_union(
            [from_str, from_none], obj.get("display_aspect_ratio"))
        pix_fmt = from_union([from_str, from_none], obj.get("pix_fmt"))
        level = from_union([from_int, from_none], obj.get("level"))
        color_range = from_union([from_str, from_none], obj.get("color_range"))
        color_space = from_union([from_str, from_none], obj.get("color_space"))
        chroma_location = from_union(
            [from_str, from_none], obj.get("chroma_location"))
        field_order = from_union([from_str, from_none], obj.get("field_order"))
        refs = from_union([from_int, from_none], obj.get("refs"))
        is_avc = from_union(
            [from_none, lambda x: from_stringified_bool(from_str(x))], obj.get("is_avc"))
        nal_length_size = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("nal_length_size"))
        r_frame_rate = from_str(obj.get("r_frame_rate"))
        avg_frame_rate = from_str(obj.get("avg_frame_rate"))
        time_base = from_str(obj.get("time_base"))
        start_pts = from_int(obj.get("start_pts"))
        start_time = from_str(obj.get("start_time"))
        bits_per_raw_sample = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("bits_per_raw_sample"))
        extradata_size = from_union(
            [from_int, from_none], obj.get("extradata_size"))
        disposition = from_dict(from_int, obj.get("disposition"))
        tags = StreamTags.from_dict(obj.get("tags"))
        sample_fmt = from_union([from_str, from_none], obj.get("sample_fmt"))
        sample_rate = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("sample_rate"))
        channels = from_union([from_int, from_none], obj.get("channels"))
        channel_layout = from_union(
            [from_str, from_none], obj.get("channel_layout"))
        bits_per_sample = from_union(
            [from_int, from_none], obj.get("bits_per_sample"))
        bit_rate = from_union(
            [from_none, lambda x: int(from_str(x))], obj.get("bit_rate"))
        return Stream(index, codec_name, codec_long_name, profile, codec_type, codec_tag_string, codec_tag, width, height, coded_width, coded_height, closed_captions, film_grain, has_b_frames, sample_aspect_ratio, display_aspect_ratio, pix_fmt, level, color_range, color_space, chroma_location, field_order, refs, is_avc, nal_length_size, r_frame_rate, avg_frame_rate, time_base, start_pts, start_time, bits_per_raw_sample, extradata_size, disposition, tags, sample_fmt, sample_rate, channels, channel_layout, bits_per_sample, bit_rate)

    def to_dict(self) -> dict:
        result: dict = {}
        result["index"] = from_int(self.index)
        result["codec_name"] = from_str(self.codec_name)
        result["codec_long_name"] = from_str(self.codec_long_name)
        if self.profile is not None:
            result["profile"] = from_union([from_str, from_none], self.profile)
        result["codec_type"] = from_str(self.codec_type)
        result["codec_tag_string"] = from_str(self.codec_tag_string)
        result["codec_tag"] = from_str(self.codec_tag)
        if self.width is not None:
            result["width"] = from_union([from_int, from_none], self.width)
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        if self.coded_width is not None:
            result["coded_width"] = from_union(
                [from_int, from_none], self.coded_width)
        if self.coded_height is not None:
            result["coded_height"] = from_union(
                [from_int, from_none], self.coded_height)
        if self.closed_captions is not None:
            result["closed_captions"] = from_union(
                [from_int, from_none], self.closed_captions)
        if self.film_grain is not None:
            result["film_grain"] = from_union(
                [from_int, from_none], self.film_grain)
        if self.has_b_frames is not None:
            result["has_b_frames"] = from_union(
                [from_int, from_none], self.has_b_frames)
        if self.sample_aspect_ratio is not None:
            result["sample_aspect_ratio"] = from_union(
                [from_str, from_none], self.sample_aspect_ratio)
        if self.display_aspect_ratio is not None:
            result["display_aspect_ratio"] = from_union(
                [from_str, from_none], self.display_aspect_ratio)
        if self.pix_fmt is not None:
            result["pix_fmt"] = from_union([from_str, from_none], self.pix_fmt)
        if self.level is not None:
            result["level"] = from_union([from_int, from_none], self.level)
        if self.color_range is not None:
            result["color_range"] = from_union(
                [from_str, from_none], self.color_range)
        if self.color_space is not None:
            result["color_space"] = from_union(
                [from_str, from_none], self.color_space)
        if self.chroma_location is not None:
            result["chroma_location"] = from_union(
                [from_str, from_none], self.chroma_location)
        if self.field_order is not None:
            result["field_order"] = from_union(
                [from_str, from_none], self.field_order)
        if self.refs is not None:
            result["refs"] = from_union([from_int, from_none], self.refs)
        if self.is_avc is not None:
            result["is_avc"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(
                x)), lambda x: from_str((lambda x: str((lambda x: is_type(bool, x))(x)).lower())(x))], self.is_avc)
        if self.nal_length_size is not None:
            result["nal_length_size"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(
                x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.nal_length_size)
        result["r_frame_rate"] = from_str(self.r_frame_rate)
        result["avg_frame_rate"] = from_str(self.avg_frame_rate)
        result["time_base"] = from_str(self.time_base)
        result["start_pts"] = from_int(self.start_pts)
        result["start_time"] = from_str(self.start_time)
        if self.bits_per_raw_sample is not None:
            result["bits_per_raw_sample"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(
                x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.bits_per_raw_sample)
        if self.extradata_size is not None:
            result["extradata_size"] = from_union(
                [from_int, from_none], self.extradata_size)
        result["disposition"] = from_dict(from_int, self.disposition)
        result["tags"] = to_class(StreamTags, self.tags)
        if self.sample_fmt is not None:
            result["sample_fmt"] = from_union(
                [from_str, from_none], self.sample_fmt)
        if self.sample_rate is not None:
            result["sample_rate"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(
                x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.sample_rate)
        if self.channels is not None:
            result["channels"] = from_union(
                [from_int, from_none], self.channels)
        if self.channel_layout is not None:
            result["channel_layout"] = from_union(
                [from_str, from_none], self.channel_layout)
        if self.bits_per_sample is not None:
            result["bits_per_sample"] = from_union(
                [from_int, from_none], self.bits_per_sample)
        if self.bit_rate is not None:
            result["bit_rate"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(
                x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.bit_rate)
        return result


class ProbeResult:
    streams: List[Stream]
    format: Format

    def __init__(self, streams: List[Stream], format: Format) -> None:
        self.streams = streams
        self.format = format

    @staticmethod
    def from_dict(obj: Any) -> 'ProbeResult':
        assert isinstance(obj, dict)
        streams = from_list(Stream.from_dict, obj.get("streams"))
        format = Format.from_dict(obj.get("format"))
        return ProbeResult(streams, format)

    def to_dict(self) -> dict:
        result: dict = {}
        result["streams"] = from_list(
            lambda x: to_class(Stream, x), self.streams)
        result["format"] = to_class(Format, self.format)
        return result


def probe_result_from_dict(s: Any) -> ProbeResult:
    return ProbeResult.from_dict(s)


def probe_result_to_dict(x: ProbeResult) -> Any:
    return to_class(ProbeResult, x)
