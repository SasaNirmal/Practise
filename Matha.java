import java.util.Scanner;

public class Matha{
	public static void main(String[] args){
		Scanner x=new Scanner(System.in);
		int i=1;
		while(i<=5)
		{System.out.println("Enter day:");
		String day= x.nextLine();
		
		String dayname=day.toUpperCase();
		
			switch(dayname)
			{
				case "MONDAY":
				case "THUESDAY":
				case "WENESDAY":
					System.out.println("Today is Your Hollyday");
				break;
				case "THESTDAY":
				case "FRIDAY":
					System.out.println("School Week");
				break;
				
				case "SATADAY":
				case "SUNDAY":
					System.out.println("Class week");
				break;
				default:
					System.out.println("Try Again");
					
			i++;
			
				
			}																	
		}
	}
}