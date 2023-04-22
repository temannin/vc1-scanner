from dataclasses import dataclass
from typing import Optional, Any, Dict, List, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class FormatTags:
    title: Optional[str] = None
    creation_time: Optional[str] = None
    encoder: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FormatTags':
        assert isinstance(obj, dict)
        title = from_union([from_str, from_none], obj.get("title"))
        creation_time = from_union([from_str, from_none], obj.get("creation_time"))
        encoder = from_union([from_str, from_none], obj.get("ENCODER"))
        return FormatTags(title, creation_time, encoder)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.creation_time is not None:
            result["creation_time"] = from_union([from_str, from_none], self.creation_time)
        if self.encoder is not None:
            result["ENCODER"] = from_union([from_str, from_none], self.encoder)
        return result


@dataclass
class Format:
    filename: Optional[str] = None
    nb_streams: Optional[int] = None
    nb_programs: Optional[int] = None
    format_name: Optional[str] = None
    format_long_name: Optional[str] = None
    start_time: Optional[str] = None
    duration: Optional[str] = None
    size: Optional[str] = None
    bit_rate: Optional[str] = None
    probe_score: Optional[int] = None
    tags: Optional[FormatTags] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Format':
        assert isinstance(obj, dict)
        filename = from_union([from_str, from_none], obj.get("filename"))
        nb_streams = from_union([from_int, from_none], obj.get("nb_streams"))
        nb_programs = from_union([from_int, from_none], obj.get("nb_programs"))
        format_name = from_union([from_str, from_none], obj.get("format_name"))
        format_long_name = from_union([from_str, from_none], obj.get("format_long_name"))
        start_time = from_union([from_str, from_none], obj.get("start_time"))
        duration = from_union([from_str, from_none], obj.get("duration"))
        size = from_union([from_str, from_none], obj.get("size"))
        bit_rate = from_union([from_str, from_none], obj.get("bit_rate"))
        probe_score = from_union([from_int, from_none], obj.get("probe_score"))
        tags = from_union([FormatTags.from_dict, from_none], obj.get("tags"))
        return Format(filename, nb_streams, nb_programs, format_name, format_long_name, start_time, duration, size, bit_rate, probe_score, tags)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.filename is not None:
            result["filename"] = from_union([from_str, from_none], self.filename)
        if self.nb_streams is not None:
            result["nb_streams"] = from_union([from_int, from_none], self.nb_streams)
        if self.nb_programs is not None:
            result["nb_programs"] = from_union([from_int, from_none], self.nb_programs)
        if self.format_name is not None:
            result["format_name"] = from_union([from_str, from_none], self.format_name)
        if self.format_long_name is not None:
            result["format_long_name"] = from_union([from_str, from_none], self.format_long_name)
        if self.start_time is not None:
            result["start_time"] = from_union([from_str, from_none], self.start_time)
        if self.duration is not None:
            result["duration"] = from_union([from_str, from_none], self.duration)
        if self.size is not None:
            result["size"] = from_union([from_str, from_none], self.size)
        if self.bit_rate is not None:
            result["bit_rate"] = from_union([from_str, from_none], self.bit_rate)
        if self.probe_score is not None:
            result["probe_score"] = from_union([from_int, from_none], self.probe_score)
        if self.tags is not None:
            result["tags"] = from_union([lambda x: to_class(FormatTags, x), from_none], self.tags)
        return result


@dataclass
class StreamTags:
    duration: Optional[str] = None
    language: Optional[str] = None
    title: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StreamTags':
        assert isinstance(obj, dict)
        duration = from_union([from_str, from_none], obj.get("DURATION"))
        language = from_union([from_str, from_none], obj.get("language"))
        title = from_union([from_str, from_none], obj.get("title"))
        return StreamTags(duration, language, title)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.duration is not None:
            result["DURATION"] = from_union([from_str, from_none], self.duration)
        if self.language is not None:
            result["language"] = from_union([from_str, from_none], self.language)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        return result


@dataclass
class Stream:
    index: Optional[int] = None
    codec_name: Optional[str] = None
    codec_long_name: Optional[str] = None
    profile: Optional[str] = None
    codec_type: Optional[str] = None
    codec_tag_string: Optional[str] = None
    codec_tag: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    coded_width: Optional[int] = None
    coded_height: Optional[int] = None
    closed_captions: Optional[int] = None
    film_grain: Optional[int] = None
    has_b_frames: Optional[int] = None
    sample_aspect_ratio: Optional[str] = None
    display_aspect_ratio: Optional[str] = None
    pix_fmt: Optional[str] = None
    level: Optional[int] = None
    color_range: Optional[str] = None
    color_space: Optional[str] = None
    color_transfer: Optional[str] = None
    color_primaries: Optional[str] = None
    chroma_location: Optional[str] = None
    refs: Optional[int] = None
    r_frame_rate: Optional[str] = None
    avg_frame_rate: Optional[str] = None
    time_base: Optional[str] = None
    start_pts: Optional[int] = None
    start_time: Optional[str] = None
    extradata_size: Optional[int] = None
    disposition: Optional[Dict[str, int]] = None
    tags: Optional[StreamTags] = None
    sample_fmt: Optional[str] = None
    sample_rate: Optional[str] = None
    channels: Optional[int] = None
    channel_layout: Optional[str] = None
    bits_per_sample: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Stream':
        assert isinstance(obj, dict)
        index = from_union([from_int, from_none], obj.get("index"))
        codec_name = from_union([from_str, from_none], obj.get("codec_name"))
        codec_long_name = from_union([from_str, from_none], obj.get("codec_long_name"))
        profile = from_union([from_str, from_none], obj.get("profile"))
        codec_type = from_union([from_str, from_none], obj.get("codec_type"))
        codec_tag_string = from_union([from_str, from_none], obj.get("codec_tag_string"))
        codec_tag = from_union([from_str, from_none], obj.get("codec_tag"))
        width = from_union([from_int, from_none], obj.get("width"))
        height = from_union([from_int, from_none], obj.get("height"))
        coded_width = from_union([from_int, from_none], obj.get("coded_width"))
        coded_height = from_union([from_int, from_none], obj.get("coded_height"))
        closed_captions = from_union([from_int, from_none], obj.get("closed_captions"))
        film_grain = from_union([from_int, from_none], obj.get("film_grain"))
        has_b_frames = from_union([from_int, from_none], obj.get("has_b_frames"))
        sample_aspect_ratio = from_union([from_str, from_none], obj.get("sample_aspect_ratio"))
        display_aspect_ratio = from_union([from_str, from_none], obj.get("display_aspect_ratio"))
        pix_fmt = from_union([from_str, from_none], obj.get("pix_fmt"))
        level = from_union([from_int, from_none], obj.get("level"))
        color_range = from_union([from_str, from_none], obj.get("color_range"))
        color_space = from_union([from_str, from_none], obj.get("color_space"))
        color_transfer = from_union([from_str, from_none], obj.get("color_transfer"))
        color_primaries = from_union([from_str, from_none], obj.get("color_primaries"))
        chroma_location = from_union([from_str, from_none], obj.get("chroma_location"))
        refs = from_union([from_int, from_none], obj.get("refs"))
        r_frame_rate = from_union([from_str, from_none], obj.get("r_frame_rate"))
        avg_frame_rate = from_union([from_str, from_none], obj.get("avg_frame_rate"))
        time_base = from_union([from_str, from_none], obj.get("time_base"))
        start_pts = from_union([from_int, from_none], obj.get("start_pts"))
        start_time = from_union([from_str, from_none], obj.get("start_time"))
        extradata_size = from_union([from_int, from_none], obj.get("extradata_size"))
        disposition = from_union([lambda x: from_dict(from_int, x), from_none], obj.get("disposition"))
        tags = from_union([StreamTags.from_dict, from_none], obj.get("tags"))
        sample_fmt = from_union([from_str, from_none], obj.get("sample_fmt"))
        sample_rate = from_union([from_str, from_none], obj.get("sample_rate"))
        channels = from_union([from_int, from_none], obj.get("channels"))
        channel_layout = from_union([from_str, from_none], obj.get("channel_layout"))
        bits_per_sample = from_union([from_int, from_none], obj.get("bits_per_sample"))
        return Stream(index, codec_name, codec_long_name, profile, codec_type, codec_tag_string, codec_tag, width, height, coded_width, coded_height, closed_captions, film_grain, has_b_frames, sample_aspect_ratio, display_aspect_ratio, pix_fmt, level, color_range, color_space, color_transfer, color_primaries, chroma_location, refs, r_frame_rate, avg_frame_rate, time_base, start_pts, start_time, extradata_size, disposition, tags, sample_fmt, sample_rate, channels, channel_layout, bits_per_sample)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.index is not None:
            result["index"] = from_union([from_int, from_none], self.index)
        if self.codec_name is not None:
            result["codec_name"] = from_union([from_str, from_none], self.codec_name)
        if self.codec_long_name is not None:
            result["codec_long_name"] = from_union([from_str, from_none], self.codec_long_name)
        if self.profile is not None:
            result["profile"] = from_union([from_str, from_none], self.profile)
        if self.codec_type is not None:
            result["codec_type"] = from_union([from_str, from_none], self.codec_type)
        if self.codec_tag_string is not None:
            result["codec_tag_string"] = from_union([from_str, from_none], self.codec_tag_string)
        if self.codec_tag is not None:
            result["codec_tag"] = from_union([from_str, from_none], self.codec_tag)
        if self.width is not None:
            result["width"] = from_union([from_int, from_none], self.width)
        if self.height is not None:
            result["height"] = from_union([from_int, from_none], self.height)
        if self.coded_width is not None:
            result["coded_width"] = from_union([from_int, from_none], self.coded_width)
        if self.coded_height is not None:
            result["coded_height"] = from_union([from_int, from_none], self.coded_height)
        if self.closed_captions is not None:
            result["closed_captions"] = from_union([from_int, from_none], self.closed_captions)
        if self.film_grain is not None:
            result["film_grain"] = from_union([from_int, from_none], self.film_grain)
        if self.has_b_frames is not None:
            result["has_b_frames"] = from_union([from_int, from_none], self.has_b_frames)
        if self.sample_aspect_ratio is not None:
            result["sample_aspect_ratio"] = from_union([from_str, from_none], self.sample_aspect_ratio)
        if self.display_aspect_ratio is not None:
            result["display_aspect_ratio"] = from_union([from_str, from_none], self.display_aspect_ratio)
        if self.pix_fmt is not None:
            result["pix_fmt"] = from_union([from_str, from_none], self.pix_fmt)
        if self.level is not None:
            result["level"] = from_union([from_int, from_none], self.level)
        if self.color_range is not None:
            result["color_range"] = from_union([from_str, from_none], self.color_range)
        if self.color_space is not None:
            result["color_space"] = from_union([from_str, from_none], self.color_space)
        if self.color_transfer is not None:
            result["color_transfer"] = from_union([from_str, from_none], self.color_transfer)
        if self.color_primaries is not None:
            result["color_primaries"] = from_union([from_str, from_none], self.color_primaries)
        if self.chroma_location is not None:
            result["chroma_location"] = from_union([from_str, from_none], self.chroma_location)
        if self.refs is not None:
            result["refs"] = from_union([from_int, from_none], self.refs)
        if self.r_frame_rate is not None:
            result["r_frame_rate"] = from_union([from_str, from_none], self.r_frame_rate)
        if self.avg_frame_rate is not None:
            result["avg_frame_rate"] = from_union([from_str, from_none], self.avg_frame_rate)
        if self.time_base is not None:
            result["time_base"] = from_union([from_str, from_none], self.time_base)
        if self.start_pts is not None:
            result["start_pts"] = from_union([from_int, from_none], self.start_pts)
        if self.start_time is not None:
            result["start_time"] = from_union([from_str, from_none], self.start_time)
        if self.extradata_size is not None:
            result["extradata_size"] = from_union([from_int, from_none], self.extradata_size)
        if self.disposition is not None:
            result["disposition"] = from_union([lambda x: from_dict(from_int, x), from_none], self.disposition)
        if self.tags is not None:
            result["tags"] = from_union([lambda x: to_class(StreamTags, x), from_none], self.tags)
        if self.sample_fmt is not None:
            result["sample_fmt"] = from_union([from_str, from_none], self.sample_fmt)
        if self.sample_rate is not None:
            result["sample_rate"] = from_union([from_str, from_none], self.sample_rate)
        if self.channels is not None:
            result["channels"] = from_union([from_int, from_none], self.channels)
        if self.channel_layout is not None:
            result["channel_layout"] = from_union([from_str, from_none], self.channel_layout)
        if self.bits_per_sample is not None:
            result["bits_per_sample"] = from_union([from_int, from_none], self.bits_per_sample)
        return result


@dataclass
class ProbeResult:
    streams: Optional[List[Stream]] = None
    format: Optional[Format] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ProbeResult':
        assert isinstance(obj, dict)
        streams = from_union([lambda x: from_list(Stream.from_dict, x), from_none], obj.get("streams"))
        format = from_union([Format.from_dict, from_none], obj.get("format"))
        return ProbeResult(streams, format)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.streams is not None:
            result["streams"] = from_union([lambda x: from_list(lambda x: to_class(Stream, x), x), from_none], self.streams)
        if self.format is not None:
            result["format"] = from_union([lambda x: to_class(Format, x), from_none], self.format)
        return result


def probe_result_from_dict(s: Any) -> ProbeResult:
    return ProbeResult.from_dict(s)


def probe_result_to_dict(x: ProbeResult) -> Any:
    return to_class(ProbeResult, x)

    

import subprocess
import json

def get_video_stream(args: List[str]) -> Stream:
    process_result = subprocess.run(args, capture_output=True)
    probe_data = json.loads(process_result.stdout.decode("utf-8"))
    probe_result = ProbeResult.from_dict(probe_data)

    for stream in probe_result.streams:
        if (stream.codec_type == "video"):
            return stream

    raise AssertionError(f"Could not find video stream in file: {args}")
