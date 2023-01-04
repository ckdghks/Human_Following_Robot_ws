

class BoundingBoxClass:

    def get_Object(bboxes):
        lenOfbbox = len(bboxes)

        square_list = [] # w * h
        index_list = []
        for i in range(lenOfbbox):
            if bboxes[i].Class == "person":
                w = bboxes[i].xmax - bboxes[i].xmin
                h = bboxes[i].ymax - bboxes[i].ymin
                square_list.append(w*h)
                index_list.append(i)
        
        if len(square_list) == 0:
            print("There is No person!!!")
            return str([])

        elif len(square_list) == 1:
            print("You're In Second Case!!!")
            bbox = [bboxes[index_list[0]].xmin, 
                    bboxes[index_list[0]].ymin,
                    bboxes[index_list[0]].xmax,
                    bboxes[index_list[0]].ymax,
                    bboxes[index_list[0]].probability]
            return str(bbox)
            
        else:
            # Calculate What is the larggest square
            # That argument is the nearest one.
            # So we traking that one.
            print("You're In Third Case!!!")
            largest_one = square_list[0]
            largestOne_index = index_list[0]

            for i in range(len(square_list)):
                if square_list[i] > largest_one:
                    largest_one = square_list[i]
                    largestOne_index = index_list[i]
            

            bbox = [bboxes[largestOne_index].xmin,
                    bboxes[largestOne_index].ymin,
                    bboxes[largestOne_index].xmax,
                    bboxes[largestOne_index].ymax,
                    bboxes[largestOne_index].probability]
            return str(bbox)
    
    def Keep_Distance(data):
        # We Subscribe relative distance information.
        # maybe 0~255.
        # we have to keep the certain distance.
        # How?
        
        return
