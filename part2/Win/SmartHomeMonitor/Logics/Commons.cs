using MahApps.Metro.Controls;
using MahApps.Metro.Controls.Dialogs;
using MQTTnet.Client;
using System.Threading.Tasks;
using System.Windows;

namespace SmartHomeMonitoringApp.Logics
{
    public class Commons
    {
        // * 참고 Window Mqtt Broker 가 설정되어있으므로, 가능한 아이피와 호스트가 만음
        // Localhost, 127.0.0.1, 192.168.5.2 
        public static string BROKERHOST { get; set; } = "192.168.5.2";  // Window Mqtt Broker Mosquitto IP
        public static string MQTTTOPIC { get; set; } = "pknu/data/"; // 대소문자 구분, 마지막 /도 중요! 
        public static string DBCONNSTRING { get; set; } = "Data Source=localhost;" +
                                                          "Initial Catalog=EMS;" +
                                                          "Persist Security Info=True;" +
                                                          "User ID=sa;" +
                                                          "Password=mssql_p@ss;" +
                                                          "Encrypt=False"; 
        public static IMqttClient MQTT_CLIENT { get; set; } // 전체 프로젝트에서 다 사용할 공용 Mqtt 클라이언트 
    }
}
