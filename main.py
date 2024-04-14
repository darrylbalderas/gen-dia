from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.storage import FsxForLustre
from diagrams.aws.database import Aurora

from diagrams.programming.language import Go
from diagrams.programming.framework import Django


def create_file_manager_api():
    title = "File Manager API with FSx for Lustre"
    with Diagram(title, show=False):
        data_storage = FsxForLustre("data_storage")

        with Cluster("File Manager API"):
            file_manager_api = Go("api")
            host = EC2("host")
            file_manager_api_deployment = host << file_manager_api

        file_manager_api_deployment >> data_storage
        file_manager_api_deployment << data_storage


def video_monitoring_app():
    title = "Video Monitoring App"
    with Diagram(title, show=False):
        video_indexes = Aurora("VideoIndex")

        with Cluster("Video Monitoring App"):
            video_monitoring_app = Django("app")
            host = EC2("host")
            video_monitoring_app_deployment = host << video_monitoring_app

        video_monitoring_app_deployment >> video_indexes
        video_monitoring_app_deployment << video_indexes


def main():
    create_file_manager_api()
    video_monitoring_app()


if __name__ == "__main__":
    main()
